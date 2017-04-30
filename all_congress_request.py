import requests 
import pandas as pd 
from pandas.io.json import json_normalize

base_url = 'https://www.govtrack.us/api/v2/'
param = 'role?current=true' #Returns senator information

r = requests.get(base_url + param + '&format=json')
data = r.json()

full_congress = json_normalize(data['objects'])
congress_ids = full_congress[['firstname', 'lastname']]




#separate senators and representatives into separate dataframes 

#return 

#dictionary["value"]["value2"]