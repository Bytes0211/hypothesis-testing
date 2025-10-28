
import pyproj
from bokeh.core.enums import enumeration
import pandas as pd 
import numpy as np

class InvalidParamEntry(Exception):
    """Raised when invalid parameter is passed"""
    
class InvalidVendor(Exception):
	"""Raised when an invalid vendor is specified"""
 
 

class Mercator: 
	
	def __init__(self, x: int | float = 0.0, y: int | float = 0.00):
		self.x = x
		self.y = y
		
  
	def mercator_to_latlon(self, x, y):
		"""
		Converts Web Mercator (EPSG:3857) x, y coordinates to WGS 84 latitude and longitude.

		Args:
			x (float): X coordinate in meters.
			y (float): Y coordinate in meters.

		Returns:
			tuple: A tuple containing the latitude and longitude in degrees.
		"""
		transformer = pyproj.Transformer.from_crs("epsg:3857", "epsg:4326", always_xy=True)
		longitude, latitude = transformer.transform(x, y)
		return latitude, longitude


	def latlon_to_mercator(self, latitude, longitude):
		"""
		Converts WGS 84 latitude and longitude to Web Mercator (EPSG:3857) x, y coordinates.

		Args:
			latitude (float): Latitude in degrees.
			longitude (float): Longitude in degrees.

		Returns:
			tuple: A tuple containing the x and y Mercator coordinates in meters.
		"""
		# Define the source (WGS 84) and destination (Web Mercator) CRSs
		transformer = pyproj.Transformer.from_crs("epsg:4326", "epsg:3857", always_xy=True)

		# Perform the transformation
		mercator_x, mercator_y = transformer.transform(longitude, latitude)

		return int(mercator_x), int(mercator_y)

	def df_to_mercator(self, df: pd.DataFrame, lon: str = 'lon', lat: str = 'lat') -> pd.DataFrame:
		# Convert dec lon/lat to web mercator format
		
		for i in range(len(df)):
			df.loc[i, 'x'], df.loc[i, 'y'] = self.latlon_to_mercator(df.loc[i, lat], df.loc[i, lon])

		return df



	def getTransform(self):
		"""
		Returns the transformation object for converting between WGS 84 and Web Mercator coordinates.

		Returns:
			pyproj.Transformer: A transformer object for coordinate conversion.
		"""
		return pyproj.Transformer.from_crs("epsg:3857", "epsg:4326", always_xy=True)



	def validateVendor(self, vendor: str = '')-> str:
		"""
		Returns the bokeh vendor listed in vendor enumeration.

		Args:
			vendor (str): The name of the vendor.

		Returns:
			str: A string containing vendor information.
		"""


		VENDORS = enumeration('CARTODBPOSITRON', 'CARTODBPOSITRON_RETINA', 'STAMEN_TERRAIN', 'STAMEN_TERRAIN_RETINA',
		                      'STAMEN_TONER', 'STAMEN_TONER_BACKGROUND', 'STAMEN_TONER_LABELS', 'OSM', 'ESRI_IMAGERY')

		if isinstance(vendor, str) and vendor.upper() in VENDORS:
			# Return the vendor information if it exists
			return vendor.upper()
		else:
			# Raise an exception if the vendor is invalid
			raise InvalidVendor(f"Invalid vendor: {vendor}. Valid vendors are: {', '.join(VENDORS)}")
  

