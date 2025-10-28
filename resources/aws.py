import uuid
import json
import boto3 as boto
import requests 
import io 
from botocore.exceptions import ClientError
from resources import util, lambdadeployer  # type: ignore

class Aws:
    """AWS service wrapper class for S3, IAM, and Lambda operations."""

    def __init__(self) -> None:
        """Initialize AWS service clients lazily."""
        self._s3_client = None 
        self._s3_resource = None
        self._iam_client = None
        self._lambda_client = None
        
    # Properties for lazy initialization of AWS clients
    # lazy initialization Creational Design Pattern that delays the creation of a resource until it’s actually needed
    @property
    def s3_client(self):
        if self._s3_client is None:
            self._s3_client = util.get_s3_client()
        return self._s3_client
    
    # @s3_client.setter allows you to define a method that will be called when you assign a value to the s3_client property.
    # syntactically useful for dependency injection during testing or when you want to override the default client behavior.
    # warning: setter methods should be used judiciously to avoid unintended side effects. Especially with multi-threaded applications, changing the client unexpectedly could lead to inconsistent behavior.
    # and methods that are resource-intensive or have side effects should be designed carefully to ensure that they behave predictably when their dependencies are changed.
    @s3_client.setter
    def s3_client(self, value):
        self._s3_client = value
    
    @property
    def s3_resource(self):
        if self._s3_resource is None:
            self._s3_resource = util.get_s3_resource()
        return self._s3_resource
    
    @s3_resource.setter
    def s3_resource(self, value):
        self._s3_resource = value

    @property
    def iam_client(self):
        if self._iam_client is None:
            self._iam_client = util.get_iam_client()
        return self._iam_client
    
    @iam_client.setter
    def iam_client(self, value):
        self._iam_client = value
    
    @property
    def lambda_client(self):
        if self._lambda_client is None:
            self._lambda_client = util.get_lambda_client()
        return self._lambda_client
    
    @lambda_client.setter
    def lambda_client(self, value):
        self._lambda_client = value

    @property
    def lambda_deployer(self):
        if self._lambda_deployer is None:
            self._lambda_deployer = lambdadeployer.LambdaDeployer()
        return self._lambda_deployer

    @lambda_deployer.setter
    def lambda_deployer(self, value):
        self._lambda_deployer = value

    def create_bucket_name(self, prefix: str = 'scotton') -> str:
        """Create unique bucket name with UUID suffix."""
        return f"{prefix}-{str(uuid.uuid4())[:8]}"

    def create_bucket(self, bucket_prefix: str) -> tuple:
        """Create S3 bucket with proper region configuration."""
        session = boto.session.Session() # type: ignore
        current_region = session.region_name
        bucket_name = self.create_bucket_name(bucket_prefix)
        
        if current_region == 'us-east-1':
            bucket_resp = self.s3_resource.create_bucket(Bucket=bucket_name)
        else:
            bucket_resp = self.s3_resource.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': current_region}
            )
        
        return bucket_name, bucket_resp

    def list_buckets(self) -> None:
        """List all S3 buckets in account."""
        response = self.s3_client.list_buckets()
        print(f"📋 S3 Buckets in account:\n")
        for bucket in response.get('Buckets', []):
            print(f" - {bucket['Name']}")

    def list_bucket_objects(self, bucket_name: str) -> None:
        """List objects in S3 bucket."""
        response = self.s3_client.list_objects_v2(Bucket=bucket_name)
        print(f"📋 S3 Objects in bucket {bucket_name}:\n")
        for obj in response.get('Contents', []):
            print(f" - {obj['Key']} (Size: {obj['Size']}, StorageClass: {obj['StorageClass']})")


    def add_file_to_bucket(self, bucket_name: str, file_name: str, object_name: str, url: str = None) -> tuple: # type: ignore
        """Upload file to S3 bucket from local path or URL."""
        if url:
            response = requests.get(f'{url}/{file_name}')
            response.raise_for_status()
            self.s3_client.upload_fileobj(io.BytesIO(response.content), bucket_name, object_name)
        else:
            with open(file_name, 'rb') as file:
                self.s3_client.upload_fileobj(file, bucket_name, object_name)
        return 200, f'✅ FILE {object_name} UPLOADED TO {bucket_name} SUCCESSFULLY!'

    def copy_to_bucket(self, from_bucket: str, to_bucket: str, file_name: str) -> str:
        """Copy S3 object between buckets."""
        copy_source = {'Bucket': from_bucket, 'Key': file_name}
        self.s3_resource.Object(to_bucket, file_name).copy(copy_source)
        return f'✅ FILE {file_name} COPIED FROM {from_bucket} TO {to_bucket}'

    def delete_files_from_bucket(self, bucket_name: str, file_list: list) -> tuple:
        """Delete multiple files from S3 bucket efficiently."""
        if not isinstance(file_list, list):
            return 400, f'❌ {file_list} IS NOT A LIST'
        
        # Use batch delete for efficiency
        delete_objects = [{'Key': key} for key in file_list]
        response = self.s3_client.delete_objects(
            Bucket=bucket_name,
            Delete={'Objects': delete_objects}
        )
        return 200, f'✅ {len(file_list)} FILES DELETED FROM {bucket_name}'

    def enable_bucket_versioning(self, bucket_name: str) -> str:
        """Enable versioning for S3 bucket."""
        versioning = self.s3_resource.BucketVersioning(bucket_name)
        versioning.enable()
        return f'✅ VERSIONING ENABLED FOR BUCKET {bucket_name} - STATUS: {versioning.status}'

    def list_iam_roles(self) -> dict:
        """List all IAM roles in account."""
        response = self.iam_client.list_roles()
        return {
            role['RoleName']: (role['RoleName'], role['Arn']) 
            for role in response['Roles']
        }

    def validate_iam_role(self, role: str) -> tuple:
        """Validate IAM role exists in account."""
        role_list = self.list_iam_roles()
        if role in role_list:
            return 1, role_list[role]
        return 0, f'❌ ROLE {role} NOT FOUND!'
    
    def invoke_function(self, function_name: str, function_params: dict, get_log: bool = False) -> dict:
        """Invokes a Lambda function."""
        try:
            response = self.lambda_client.invoke(
                FunctionName=function_name,
                Payload=json.dumps(function_params),
                LogType="Tail" if get_log else "None",
            )
            print(f"✅ Function {function_name} invoked successfully")
            return response
        except ClientError as err:
            print(f"❌ Error invoking function {function_name}: {err.response['Error']['Code']} - {err.response['Error']['Message']}")
            raise
    
    def update_function_code(self, function_name: str, deployment_package: bytes) -> None:
        """Updates Lambda function code with .zip archive."""
        try:
            print(f"✅ Function {function_name} code updated successfully")
            self.lambda_client.update_function_code(
                FunctionName=function_name, ZipFile=deployment_package
            )
        except ClientError as err:
            print(f"❌ Error updating function {function_name}: {err.response['Error']['Code']} - {err.response['Error']['Message']}")
            raise
    
    def update_function_configuration(self, function_name: str, env_vars: dict) -> None:
        """Updates Lambda function environment variables."""
        try:
            response = self.lambda_client.update_function_configuration(
                FunctionName=function_name, Environment={"Variables": env_vars}
            )
            print(f'✅ Function {function_name} configuration updated successfully')
            return response
        except ClientError as err:
            print(f"❌ Error updating function config {function_name}: {err.response['Error']['Code']} - {err.response['Error']['Message']}")
            raise
    
    def list_functions(self) -> None:
        """
        Lists the Lambda functions for the current account.
        Returns list of function details.
        """
        try:
            func_paginator = self.lambda_client.get_paginator("list_functions")
            for page in func_paginator.paginate():
                print(f"📋 Functions in account:\n")
                for func in page['Functions']:
                    print(f"Function Name: {func['FunctionName']}\n"
                          f"\tDescription: {func.get('Description', '')}\n"
                          f"\tRuntime: {func['Runtime']}\n"
                          f"\tHandler: {func['Handler']}\n")
        except ClientError as err:
            print(f"❌ Error listing functions: {err.response['Error']['Code']} - {err.response['Error']['Message']}")
            
