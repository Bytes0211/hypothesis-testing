class InvalidKeyError(Exception):
    """Raised when invalid type is passed as a key """
    pass 

class InvalidKeyValueError(Exception):
    """Raised when invalid type is passed as a key """
    pass 

class InvalidSampleSize(Exception):
    """Raised when invalid type is passed as a key """
    pass 

class InvalidHypothesisType(Exception):
    """Raised when invalid type is passed as a key """
    pass 


class Test:
    def __init__(self) -> None:
        self.test = '' # hypothesis or critical_value
        self.type = '' # type of test: difference of mean(diff), mean(mean), or proportional(prop) 
        self.tail = '' # type of test 
        self.sigma1 = 0 # population standard deviation 
        self.sigma2 = 0
        self.N = 0
        self.n1 = 0 # sample 1
        self.n2 = 0 # sample 2 (for diff of means)
        self.xbar1 = 0 # sample mean 1
        self.xbar2 = 0 # sample of mean 2 for diff of mean
        self.p = 0 # proportion of population 
        self.p_hat = 0 # sample proportion 
        self.s1 = 0 # sample standard deviation 
        self.s2 = 0 # sample standard deviation for diff mean
        self.hypothesize_diff = 0 # hypothesized value
        self.cl = 0 # confidence level
        self.alpha = 0 # 
        self.equal_variances = None  # diff of mean value check if variances are equal  
        self.var1 = 0  # sample variance 
        self.var2 = 0 # sample variance for diff of mean 
        self.diff_of_means = 0 # diff or means for diff of mean hypo testing
        self.pooled_variance = 1 # pooled variance (S_p) - I set this to 1 so that even if its called without calc no harm
        self.std_err = 0
        self.df = 0 # degrees of freedom
        self.q = 0 # area , used to calculate a, and t values
        self.ci = 0 # confidence interval 
        self.a = 0 # confidence interval lower value 
        self.b = 0 # confidence interval upper value 
        self.critical_value = 0 # critical value of z or t test 
        self.test_statistic = 0 # diff of mean - hypothesized diff of mean / standard error 
        self.t_test = 0
        self.frac1 = 0
        self.frac2 = 0
        self.me = 0 # margin of error used to calculate minimum sample size required for confidence interval SDSM 
        self.min_n = 0 # minimal sample size for sample mean test 
        self.mar_err_min_n = 0 # the suggested margin of error when calculating minimum sample size
        self.replacement = False
        self.fpc = 0 
        self.z = True
        self.size = '' # large or small sample size - calculated
        self.sample_ratio = 0 # calculated n/N 
        self.successes = 0
        self.failures = 0
        self.data = {}
        


    def make_hypothesis_test(self, info : dict = {}, statement : bool = False, visual : bool = False, message : str = ''):

        self.validate_sample_data(info = info)
        self.calculate_hypothesis_test_statisics()
        if statement:
            import sys
            sys.path.insert(0, '..')
            import resources.message as message
            state = message.Statement(self.data)
            state.create_statement()
        if not statement and not visual:
            if self.type == 'mean':
                msg = f'N: {self.N}\nn: {self.n1}\nxbar: {self.xbar1}\nSigma: {self.sigma1}\nCL: {self.cl}\n'
                msg = msg + f'critical_value:{self.critical_value}\nstd_err: {self.std_err}\nfpc: {self.fpc}\nme: {self.me} '
                print(msg)
            if self.type == "diff_of_mean":
                msg = f'Hypothesis Test: {self.type}\n'
                msg = f'sigma1: {self.sigma1}\nsigma2: {self.sigma2}\nxbar1: {self.xbar1}\nxbar2: {self.xbar2}\ns1: {self.s1}\ns2: {self.s2}\n'
                msg = msg + f'var1: {self.var1}\nvar2: {self.var2}\nn1: {self.n1}\nn2: {self.n2}\nstandard error: {self.std_err}\n'
                msg = msg + f'pooled varience: {self.pooled_variance}\ncritical_value: {self.critical_value}\nmargin of error: {self.me}\n'
                msg = msg + f'(a, b) = ({self.a}, {self.b})'
                print(msg)
            if self.type == 'prop':
                msg = f'N: {self.N}\nn: {self.n1}\nsample ratio: {self.sample_ratio}\nsuccesses: {self.successes}\n'
                msg = msg + f'failures: {self.failures}\np_hat: {self.p_hat}\nconfidence level: {self.cl}\nstandard error: {self.std_err}\n'
                msg = msg + f'critical value: {self.critical_value}\nfpc: {self.fpc}\nmargin of error: {self.me}\n'
                msg = msg + f'(a, b) = ({self.a}, {self.b})'
                print(msg)


    def make_critical_test(self, info : dict = {}, statement : bool = False, visual : bool = False, message : str = ''):

        self.validate_sample_data(info = info)
        self.calculate_critical_value_test_statisics()
        if statement:
            import sys
            sys.path.insert(0, '..')
            import resources.message as message
            state = message.Statement(self.data)
            state.create_statement()
        if not statement and not visual:
            if self.type == 'mean':
                msg = f'N: {self.N}\nn: {self.n1}\nxbar: {self.xbar1}\nSigma: {self.sigma1}\nCL: {self.cl}\n'
                msg = msg + f'critical_value:{self.critical_value}\nstd_err: {self.std_err}\nfpc: {self.fpc}\nme: {self.me} '
                print(msg)
            if self.type == "diff_of_mean":
                msg = f'difference of mean: {self.diff_of_means}\nhypothesize difference: {self.hypothesize_diff}\n'
                msg = msg + f'standard deviation: {self.std_err}\nsample size: {self.size}\n'
                msg = msg + f'equal variances: {self.equal_variances}\n'
                msg = msg + f't test score of the difference of sample1 and sample2 is: {self.t_test}\n'
                msg = msg + f'degrees of freedom: {self.df}\n'
                msg = msg + f'critical value t test score: {self.critical_value}\n'
                print(msg)
            if self.type == 'prop':
                msg = f'N: {self.N}\nn: {self.n1}\nsample ratio: {self.sample_ratio}\nsuccesses: {self.successes}\n'
                msg = msg + f'failures: {self.failures}\np_hat: {self.p_hat}\nconfidence level: {self.cl}\nstandard error: {self.std_err}\n'
                msg = msg + f'critical value: {self.critical_value}\nfpc: {self.fpc}\nmargin of error: {self.me}\n'
                print(msg)


    def validate_sample_data(self, info : dict = {}):
        validate = {}
        keyList = ['test','type', 'tail', 'replacement', 'N', 'sigma1', 'sigma2', 'n1', 'n2', 'xbar1', 'xbar2', 
                   'p', 'p_hat', 'hypothesize_diff', 's1', 's2', 'cl', 'mar_err_min_n']
        for key in keyList:
            validate[key] = None 
        if isinstance(info, dict) and len(info.keys()) > 0:
            for key, val in info.items():
                if key in validate: 
                    if key == "test":
                        if not isinstance(val, str):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL
                            raise InvalidKeyValueError  
                        else:
                            if info['test'].lower() in ['hypothesis', 'critical_value']:
                                self.test = info['test'].lower()
                            else:
                                from colorama import Fore, Style
                                print(Fore.RED, Style.BRIGHT + f'Invalid Hypothesis test \nChoices are "hypothesis", "critical_value" ')
                                Style.RESET_ALL
                                raise InvalidHypothesisType 
                    ############
                    if key == "type":
                        if not isinstance(val, str):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL
                            raise InvalidKeyValueError  
                        else:
                            if info['type'].lower() in ["diff_of_mean", 'mean', 'prop']:
                                self.type = info['type'].lower()
                            else:
                                from colorama import Fore, Style
                                print(Fore.RED, Style.BRIGHT + f'Invalid Hypothesis test type\nChoices are "diff", "mean", and "prop" ')
                                Style.RESET_ALL
                                raise InvalidHypothesisType 
                    if key == "tail":
                        if not isinstance(val, str):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL
                            raise InvalidKeyValueError  
                        else:
                            self.tail = info['tail']
                            
                    if key == "replacement":
                        if not isinstance(val, bool):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL
                            raise InvalidKeyValueError  
                        else:
                            self.tail = info['replacement']

                    if key == "mar_err_min_n":
                        if not isinstance(val, int):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL
                            raise InvalidKeyValueError  
                        else:
                            self.mar_err_min_n = info['mar_err_min_n']                            
                            
                    if key == "sigma1":
                        if not isinstance(val, int | float):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL
                            raise InvalidKeyValueError   
                        else:
                            self.sigma1 = info['sigma1']
                    if key == "N":
                        if not isinstance(val, int | float):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL
                            raise InvalidKeyValueError   
                        else:
                            self.N = info['N']
                    if key == "sigma2":
                        if not isinstance(val, int | float):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL
                            raise InvalidKeyValueError   
                        else:
                            self.sigma2 = info['sigma2']
                    if key == "n1":
                        if not isinstance(val, int):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL                        
                            raise InvalidKeyValueError
                        else: 
                            self.n1 = info['n1']
                    if key == "n2":
                        if not isinstance(val, int):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL                        
                            raise InvalidKeyValueError
                        else: 
                            self.n2 = info['n2']
                    if key == "xbar1":
                        if not isinstance(val, int | float):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL                        
                            raise InvalidKeyValueError
                        else: 
                            self.xbar1 = info['xbar1']
                    if key == "xbar2":
                        if not isinstance(val, int | float):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL                        
                            raise InvalidKeyValueError  
                        else: 
                            self.xbar2 = info['xbar2']  
                    if key == "p":
                        if not isinstance(val, int | float):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL                        
                            raise InvalidKeyValueError  
                        else: 
                            self.p = info['p']  
                            
                    if key == "p_hat":
                        if not isinstance(val, int | float):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL                        
                            raise InvalidKeyValueError  
                        else: 
                            self.p_hat = info['p_hat']  
                    if key == "s1":
                        if not isinstance(val, int | float):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL                        
                            raise InvalidKeyValueError   
                        else: 
                            self.s1 = info['s1']  
                    if key == "s2":
                        if not isinstance(val, int | float):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL                        
                            raise InvalidKeyValueError   
                        else: 
                            self.s2 = info['s2']
                    if key == "cl":
                        if not isinstance(val, int | float):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL                        
                            raise InvalidKeyValueError   
                        else: 
                            self.cl = info['cl']
                    if key == "hypothesize_diff":
                        if not isinstance(val, int | float):
                            from colorama import Fore, Style
                            print(Fore.RED, Style.BRIGHT + f'Key: {key} with Value{val} is an invalid value.')
                            Style.RESET_ALL                        
                            raise InvalidKeyValueError   
                        else: 
                            self.hypothesize_diff = info['hypothesize_diff']
                else:
                    from colorama import Fore, Style
                    print(Fore.RED, Style.BRIGHT + f'KEY {key} IN DICTIIONARY NOT DEFINED')
                    Style.RESET_ALL    
                    raise InvalidKeyError      
        else:
            from colorama import Fore, Style
            print(Fore.RED, Style.BRIGHT + f'INFO DICTIIONARY NOT DEFINED')
            Style.RESET_ALL    
            raise InvalidKeyError  
        
        # validate  confidence level
        if self.cl < 0.01 or self.cl > .99:
            from colorama import Fore, Style
            print(Fore.RED, Style.BRIGHT + f'Invalid Confidence Level Value2: {self.cl}')
            print(Style.RESET_ALL)
            raise InvalidKeyValueError
        
        # if type is not proportion sigma1 or sxbar
        if self.type != 'prop' and self.sigma1 == 0 and self.xbar1 == 0:
            from colorama import Fore, Style
            print(Fore.RED, Style.BRIGHT + f'both population standard deviation and sample standard deviation cannot be 0')
            print(Style.RESET_ALL)
            raise InvalidHypothesisType
        
        if self.type == "diff_of_mean" and self.test == "hypothesis":
            # check to see if both sigma values are present of both s values are present
            if self.sigma1 == 0 and self.sigma2 == 0:
                if self.xbar1 == 0 and self.xbar2 == 0:
                    from colorama import Fore, Style
                    print(Fore.RED, Style.BRIGHT + f'both population standard deviation 1 and 2OR both sample standard devations 1 and 2 must be provided')
                    print(Style.RESET_ALL)
                    raise InvalidHypothesisType   
                
            # validate xbar1 and xbar2 require valid values 
            if self.n1 == 0 and self.n2 == 0:
                from colorama import Fore, Style
                print(Fore.RED, Style.BRIGHT + f'sample size 1 and sample size 2 are required for difference of mean test')
                print(Style.RESET_ALL)
                raise InvalidHypothesisType                    

            #determine sample size  
            if (self.n1 > 29) and (self.n2 > 29):
                self.size = 'large'
            elif(self.n1 > 4) and (self.n2 > 4):
                self.size = 'small'
            else:
                raise InvalidSampleSize     
        if self.type == 'diff_of_mean' and self.test == 'critical_value':
            if any([self.n1 == 0, self.n2 == 0, self.xbar1 == 0, self.xbar2 == 0, self.s1 == 0, self.s2 == 0]):
                    from colorama import Fore, Style
                    msg = f'n1, n2, xbar1, and xbar2 all are required fields for critival_value test'
                    msg = msg + f'n1: {self.n1}, n2: {self.n2}\nxbar1: {self.xbar1}, xbar2: {self.xbar2}'
                    print(Fore.RED, Style.BRIGHT + msg)
                    print(Style.RESET_ALL)
                    raise InvalidKeyValueError   

            #determine sample size  
            if (self.n1 > 29) and (self.n2 > 29):
                self.size = 'large'
            elif(self.n1 > 4) and (self.n2 > 4):
                self.size = 'small'
            else:
                raise InvalidSampleSize   
             
            self.var1 = self.s1**2
            self.var2 = self.s2**2
        if self.type == 'prop':
            if self.p == 0 and self.p_hat == 0:         
                    from colorama import Fore, Style
                    msg = f'For Proportion Hypothesis Test, Either "p" or "p_hat" must be a valid value\n'
                    msg = msg + f'p: {self.p}, p_hat: {self.p_hat}'
                    print(Fore.RED, Style.BRIGHT + msg)
                    print(Style.RESET_ALL)
                    raise InvalidHypothesisType    
            if self.N == 0 or self.n1 == 0:
                    from colorama import Fore, Style
                    msg = f'For Proportion Hypothesis Test, Either "N" or "nt" must be a valid value\n'
                    msg = msg + f'N: {self.N}, n: {self.n1}'
                    print(Fore.RED, Style.BRIGHT + msg)
                    print(Style.RESET_ALL)
                    raise InvalidHypothesisType  
                 
                


    def calculate_hypothesis_test_statisics(self,):
        import numpy as np 
        import sys 
        sys.path.insert(0, "..")
        import resources.datum as datum 

        data = datum.Data()
    
        # calculate alpha 
        if self.tail == 'two':
            self.alpha = (1 - self.cl) / 2
        else: 
            self.alpha = 1 - self.cl        
            
        # if type is difference of mean
        if self.type == "diff_of_mean":
            self.diff_of_means = self.xbar1 - self.xbar2
            if self.sigma1 > 0 and self.sigma2 > 0: 
                frac1 = self.sigma1**2 / self.n1
                frac2 = self.sigma2**2 / self.n2
                self.std_err = np.sqrt((frac1 + frac2))
                # sample size to consider with known population standard deviations  so use z table for 
                self.critical_value = data.get_z_confidencd_level_critical_value(x = self.cl)
                self.me = self.critical_value * self.std_err
                self.a, self.b = (self.diff_of_means + self.me) , (self.diff_of_means - self.me)

            elif self.sigma1 == 0 and self.sigma2 == 0:
                # check to see if this a diff_of mean with unknown sigmas
                #calculate difference of mean
                self.diff_of_means = (self.xbar1 - self.xbar2)               
                # determine if variances are mostly equal 

                if ((self.s1**2 / self.s2**2) > 2) or ((self.s2**2 / self.s1**2) > 2):
                    self.equal_variances = False
                    frac1 = (self.s1**2 / self.n1)
                    frac2 = (self.s2**2 / self.n2)
                    self.std_err = np.sqrt((frac1 + frac2))
                    if self.size == 'large':
                        self.critical_value = data.get_z_confidencd_level_critical_value(x = self.cl)
                    else: 
                        nom = (frac1 + frac2)**2
                        denom = ((1 / (self.n1 - 1)) * (frac1)**2) + ((1 / (self.n2 - 1)) * (frac2)**2)  
                        self.df = np.floor(nom / denom )
                        print(self.cl, self.df)
                        self.critical_value = data.get_t_confidencd_level_critical_value(x = self.cl, df = self.df)
                    self.me = self.critical_value * self.std_err
                else:
                    self.equal_variances = True 
                    sp = ((self.n1 - 1) * self.var1) + ((self.n2 - 1) *  self.var2) / (self.n1 + self.n2 - 2)
                    self.pooled_variance = np.sqrt(sp)
                    frac1 = 1 / self.n1
                    frac2 = 1 / self.n2
                    self.std_err = np.sqrt((frac1 + frac2))

                    if self.size == 'large':
                        self.critical_value = data.get_z_confidencd_level_critical_value(x = self.cl)
                    else:
                        self.df = self.n1 + self.n2 - 2
                        self.critical_value = data.get_t_confidencd_level_critical_value(x= self.cl, df = self.df)
                        
                    self.me = self.critical_value * self.pooled_variance * self.std_err

            else:
                from colorama import Fore, Style
                print(Fore.RED, Style.BRIGHT + f'Bad parameter configuration for {self.type} test')
                print(Style.RESET_ALL)
                raise InvalidHypothesisType
        # TYPE = MEAN
        elif self.type == 'mean':    

            #determine sample size  
            if (self.n1 > 29):
                self.size = 'large'
            elif(self.n1 > 4):
                self.size = 'small'
                self.t = True 
            else:
                raise InvalidSampleSize
            
           
            # calculate standard error

            # check for finite population 
            if self.N > 0: 
                # if population standard deviation
                if self.sigma1 > 0:
                    # check to sample percentage for fpc 
                    if self.n1/self.N < 0.05 :
                        self.std_err = (self.sigma1/(np.sqrt(self.n1)))
                    else:
                        if self.replacement == False:
                            self.std_err = (self.sigma1/(np.sqrt(self.n1)))
                            self.fpc =  (np.sqrt((self.N - self.n1)/(self.N - 1)))
                            self.size = "small"
                        else:
                            self.std_err = self.sigma1/(np.sqrt(self.n1))
                else: 
                    if self.n1/self.N < 0.05:
                        self.std_err = (self.s1/np.sqrt(self.n1))
                    else: 
                        if self.replacement == False:
                            self.std_err = (self.s1/(np.sqrt(self.n1)))
                            self.fpc = (np.sqrt((self.N - self.n1)/(self.N - 1)))
                            self.size = "small"
                        else:
                            self.std_err = (self.s1/(np.sqrt(self.n1)))
            else:
                if self.sigma1 > 0: 
                    self.std_err = (self.sigma1/(np.sqrt(self.n1)))
                else:
                    self.std_err = (self.s1/(np.sqrt(self.n1)))


            # get critical value 
            if self.size == 'large':
                self.critical_value = data.get_z_confidencd_level_critical_value(self.cl)
            else:
                self.df = self.n1 - 1
                self.critical_value = data.get_t_confidencd_level_critical_value(x = self.cl, df = self.df)
            
            # calculate margin of error which will be used to calculate the minimum sample size
            if self.fpc > 0:
                self.me = self.critical_value * self.std_err * self.fpc
            else:
                self.me = self.critical_value * self.std_err 
         
            # calculate minimum sample size (n):
            self.min_n = np.floor(((self.critical_value * self.std_err) / self.mar_err_min_n)**2)
            
        elif self.type == 'prop':
            # get sample ratio
            self.sample_ratio = self.n1/self.N 
            
            # calculate successes and failures
            self.successes = self.p
            self.failures = self.n1 - self.successes

            # if successes and failures are less than 5, the test cannot continue
            if self.successes < 5 or self.failures < 5:
                sys.exit('Successes and Fauilurs must be greater than 5')  

            self.p_hat = self.successes / self.n1 
            
            # if sample ratio greater than 5 % set fpc 
            if self.sample_ratio > 0.05:
                self.fpc = np.sqrt((self.N - self.n1) / (self.N - 1))
            
            # set standard error
            self.std_err = np.sqrt(((self.p_hat * (1 - self.p_hat)) / self.n1))
            
            # get critical value
            self.critical_value = data.get_z_confidencd_level_critical_value(x = self.cl)
            
            # calculate margin of error
            if self.fpc > 0:
                self.me = self.critical_value * self.std_err * self.fpc 
            else:
                self.me = self.critical_value * self.std_err 

            self.a, self.b = self.p_hat - self.me, self.p_hat + self.me
        else:
            from colorama import Fore, Style
            print(Fore.RED, Style.BRIGHT + f'Hypothesis type: {self.type} not found!')
            Style.RESET_ALL
            raise InvalidHypothesisType  
        
        self.data['test'] = self.test     
        self.data['type'] = self.type
        self.data['tail'] = self.tail
        self.data['replacement'] = self.replacement
        self.data['sigma1'] = self.sigma1
        self.data['sigma2'] = self.sigma2
        self.data['n1'] = self.n1
        self.data['n2'] = self.n2
        self.data['xbar1'] = self.xbar1
        self.data['xbar2'] = self.xbar2
        self.data['p_hat'] = self.p_hat
        self.data['p'] = self.p 
        self.data['s1'] = self.s1
        self.data['s2'] = self.s2
        self.hypothesize_diff = 0 # hypothesized value
        self.data['cl'] = self.cl
        self.data['alpha'] = self.alpha # 
        self.data['equal_variances'] = self.equal_variances # diff of mean value check if variances are equal  
        self.data['var1'] = self.var1  # sample variance 
        self.data['var2'] = self.var2 # sample variance for diff of mean 
        self.data['diff_of_means'] = self.diff_of_means  # diff or means for diff of mean hypo testing
        self.data['pooled_variance'] = self.pooled_variance  # pooled variance for diff of mean (S_p)
        self.data['std_err'] = self.std_err
        self.data['df'] = self.df # degrees of freedom
        self.data['q'] = self.q # area , used to calculate a, and t values
        self.data['ci'] = self.ci # confidence interval 
        self.data['a'] = self.a # confidence interval lower value 
        self.data['b'] = self.b # confidence interval upper value 
        self.data['critical_value'] = self.critical_value # critical value of z or t test 
        self.data['frac1'] = self.frac1
        self.data["frac2"] = self.frac2
        self.data['min_n'] = self.min_n  
        self.data['mar_err_min_n'] = self.mar_err_min_n



    def calculate_critical_value_test_statisics(self,):
        import numpy as np 
        import sys 
        sys.path.insert(0, "..")
        import resources.datum as datum 

        data = datum.Data()
    
        # calculate alpha 
        if self.tail == 'two':
            self.alpha = (1 - self.cl) / 2
        else: 
            self.alpha = 1 - self.cl        
            
        # if type is difference of mean
        if self.type == "diff_of_mean":
            
            # check to see if this a diff_of mean with unknown sigmas
            #calculate difference of mean
            self.diff_of_means = (self.xbar1 - self.xbar2)               
            # determine if variances are mostly equal 

            if ((self.var1 / self.var2) > 2 or (self.var2 / self.var1) > 2):
                # unequal variances
                self.equal_variances = False
                frac1 = self.var1 / self.n1
                frac2 = self.var2 / self.n2
                self.std_err = np.sqrt((frac1 + frac2))
                if self.size == 'large':
                    self.t_test = (self.diff_of_means - self.hypothesize_diff) / self.std_err
                    self.critical_value = data.get_z_critical_value(x = self.alpha)
                else: 
                    self.t_test = (self.diff_of_means - self.hypothesize_diff) / self.std_err
                    nom = (frac1 + frac2)**2
                    denom = ((1 / (self.n1 - 1)) * frac1**2) + ((1 / (self.n2 - 1)) * frac2**2)
                    self.df = int(np.floor(nom/denom )) # round down degrees of freedom 
                    self.critical_value = data.get_t_critical_value(tail = self.tail, q = self.alpha, df = self.df)
                self.me = self.test_statistic * self.std_err
            else:
                # equal variances
                self.equal_variances = True 
                sp = ((self.n1 - 1) * self.var1) + ((self.n2 - 1) *  self.var2) / (self.n1 + self.n2 - 2)
                self.pooled_variance = np.sqrt(sp)
                frac1 = 1 / self.n1
                frac2 = 1 / self.n2
                self.std_err = np.sqrt((frac1 + frac2))

                if self.size == 'large':
                    self.t_test = (self.diff_of_means - self.hypothesize_diff) / self.std_err
                    self.critical_value = data.get_z_critical_value(x = self.alpha)
                else:
                    self.t_test = (self.diff_of_means - self.hypothesize_diff) / self.std_err
                    self.df = self.n1 + self.n2 - 2
                    self.critical_value = data.get_t_critical_value(tail = self.tail, q = self.alpha, df = self.df)
        elif self.type == 'mean':    

            # check for finite population 
            if self.N > 0: 
                # if population standard deviation
                if self.sigma1 > 0:
                    # check to sample percentage for fpc 
                    if self.n1/self.N < 0.05 :
                        self.std_err = (self.sigma1/(np.sqrt(self.n1)))
                    else:
                        if self.replacement == False:
                            self.std_err = (self.sigma1/(np.sqrt(self.n1)))
                            self.fpc =  (np.sqrt((self.N - self.n1)/(self.N - 1)))
                            self.size = "small"
                        else:
                            self.std_err = self.sigma1/(np.sqrt(self.n1))
                else: 
                    if self.n1/self.N < 0.05:
                        self.std_err = (self.s1/np.sqrt(self.n1))
                    else: 
                        if self.replacement == False:
                            self.std_err = (self.s1/(np.sqrt(self.n1)))
                            self.fpc = (np.sqrt((self.N - self.n1)/(self.N - 1)))
                            self.size = "small"
                        else:
                            self.std_err = (self.s1/(np.sqrt(self.n1)))
            else:
                if self.sigma1 > 0: 
                    self.std_err = (self.sigma1/(np.sqrt(self.n1)))
                else:
                    self.std_err = (self.s1/(np.sqrt(self.n1)))


            # get critical value 
            if self.size == 'large':
                self.critical_value = data.get_z_confidencd_level_critical_value(self.cl)
            else:
                self.df = self.n1 - 1
                self.critical_value = data.get_t_confidencd_level_critical_value(x = self.cl, df = self.df)
            
            # calculate margin of error which will be used to calculate the minimum sample size
            if self.fpc > 0:
                self.me = self.critical_value * self.std_err * self.fpc
            else:
                self.me = self.critical_value * self.std_err 
         
            # calculate minimum sample size (n):
            self.min_n = np.floor(((self.critical_value * self.std_err) / self.mar_err_min_n)**2)
            
        elif self.type == 'prop':
            # get sample ratio
            self.sample_ratio = self.n1/self.N 
            
            # calculate successes and failures
            self.successes = self.p
            self.failures = self.n1 - self.successes

            # if successes and failures are less than 5, the test cannot continue
            if self.successes < 5 or self.failures < 5:
                sys.exit('Successes and Fauilurs must be greater than 5')  

            self.p_hat = self.successes / self.n1 
            
            # if sample ratio greater than 5 % set fpc 
            if self.sample_ratio > 0.05:
                self.fpc = np.sqrt((self.N - self.n1) / (self.N - 1))
            
            # set standard error
            self.std_err = np.sqrt(((self.p_hat * (1 - self.p_hat)) / self.n1))
            
            # get critical value
            self.critical_value = data.get_z_confidencd_level_critical_value(x = self.cl)
            
            # calculate margin of error
            if self.fpc > 0:
                self.me = self.critical_value * self.std_err * self.fpc 
            else:
                self.me = self.critical_value * self.std_err 

            self.a, self.b = self.p_hat - self.me, self.p_hat + self.me
        else:
            from colorama import Fore, Style
            print(Fore.RED, Style.BRIGHT + f'Hypothesis type: {self.type} not found!')
            Style.RESET_ALL
            raise InvalidHypothesisType  
        
        self.data['test'] = self.test 
        self.data['type'] = self.type
        self.data['tail'] = self.tail
        self.data['replacement'] = self.replacement
        self.data['sigma1'] = self.sigma1
        self.data['sigma2'] = self.sigma2
        self.data['n1'] = self.n1
        self.data['n2'] = self.n2
        self.data['xbar1'] = self.xbar1
        self.data['xbar2'] = self.xbar2
        self.data['p_hat'] = self.p_hat
        self.data['p'] = self.p 
        self.data['s1'] = self.s1
        self.data['s2'] = self.s2
        self.data['cl'] = self.cl
        self.data['alpha'] = self.alpha # 
        self.data['equal_variances'] = self.equal_variances # diff of mean value check if variances are equal  
        self.data['var1'] = self.var1  # sample variance 
        self.data['var2'] = self.var2 # sample variance for diff of mean 
        self.data['diff_of_means'] = self.diff_of_means  # diff or means for diff of mean hypo testing
        self.data['pooled_variance'] = self.pooled_variance  # pooled variance for diff of mean (S_p)
        self.data['std_err'] = self.std_err
        self.data['df'] = self.df # degrees of freedom
        self.data['q'] = self.q # area , used to calculate a, and t values
        self.data['ci'] = self.ci # confidence interval 
        self.data['a'] = self.a # confidence interval lower value 
        self.data['b'] = self.b # confidence interval upper value 
        self.data['critical_value'] = self.critical_value # critical value of z or t test 
        self.data['frac1'] = self.frac1
        self.data["frac2"] = self.frac2
        self.data['min_n'] = self.min_n  
        self.data['mar_err_min_n'] = self.mar_err_min_n



            
        


