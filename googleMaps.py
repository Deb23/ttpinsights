from geopandas import GeoDataFrame
import pandas as pd 
import geocoder 
import googlemaps
from shapely.geometry import Point
from geojsonio import display


# authentication initialized
# gmaps = googlemaps.Client(key='[your-own-key]')