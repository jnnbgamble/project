import requests 
import pandas as pd 
from pandas.io.json import json_normalize

base_url = 'https://www.govtrack.us/api/v2/'
param = 'role?current=true' #Returns senator information

r = requests.get(base_url + param + '&format=json&limit=1000')
congress_full_data = r.json()

#Collects all IDs in one place
full_congress = json_normalize(congress_full_data['objects'])
congress_ids = full_congress[['person.firstname', 'person.lastname', 'person.osid', 'person.pvsid', 'person.bioguideid']]
congress_ids = congress_ids.set_index(['person.bioguideid'])

#r2 = requests.get('http://www.opensecrets.org/api/?method=candContrib&cid=N00007360&cycle=2016&apikey=806206d71fc3b036b29ea330e74c82e0&format=json')
#data2 = r2.json()

#lobbyist_cols = ['UniqID', 'Lobbyist_raw', 'Lobbyist_stand', 'Lobbyist_id', 'year', 'Official_position', 'CID', 'Former_cong_mem']
#lobbyists = pd.read_csv('./data/lob_lobbyist.txt', sep='|,|', error_bad_lines=False, names=lobbyist_cols)



path = './data/all_industries.txt'
ic_names = ['catcode', 'catname', 'catorder', 'industry', 'sector', 'sector long']
industry_codes = pd.read_csv(path, sep='\t', names=ic_names)
#industry_codes = industry_codes.set_index('catorder')

temp = industry_codes[['catorder', 'industry']]
a =  industry_codes.industry.value_counts()

#count of the number of lobbyists in each year 

#separate senators and representatives into separate dataframes 

