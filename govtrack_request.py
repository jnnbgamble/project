import requests 
import pandas as pd 
import numpy as np

base_url = 'https://www.govtrack.us/api/v2/'
param = 'person/400054' #Returns Senator Richard Burr
all_congress = 'https://www.govtrack.us/api/v2/role?current=true'

r = requests.get(base_url + param + '/format=json') # returns everything about Senator Burr
#r2 = requests.get(all_congress) Trying to get at all of congress

#http://bioguide.congress.gov/biosearch/biosearch.asp <- Bio directory of Congress. Contains all user IDs
#Center for Responsive Politics API- https://www.opensecrets.org/resources/create/api_doc.php
#Vote Smart API- http://votesmart.org/share/api#.WOfkHBLyvq0
#Question: is there a correlation between lobbyist efforts and voting records? Of course there
#is. But how strong is it? Is there a correlation between that and twitter behavior? 

#OpenSecrets: Run by the Center for Responsive Politics. Tracks the effects of money and  
#lobbying on elections and public policy (osid from govtrack). Project vote smart also has
#information on all congresspeople

#Scraped info from bioguide https://gist.github.com/dannguyen/06aa137bf9361a3d1ce1

data = r.json()
print data
print 'name = ' + data['firstname'] + ' ' + data['lastname'] + '\nosid = ' + data['osid'] + '\npvsid = ' + data['pvsid']


#data2 = r2.json()
#print data2


#voting_records = pd.DataFrame(congress id / bills)

#Get bills that each congress person has voted for
#Use D3 for visualizations (data frames have a "to csv" method that you can use)
#Also you may be able to use mpld3 (bring matplotlib to browser):http://stackoverflow.com/questions/23659234/how-to-move-my-pandas-dataframe-to-d3

#Returns some info about Burr
#r2 = requests.get('http://www.opensecrets.org/api/?method=candIndustry&cid=N00002221&cycle=2016&apikey=806206d71fc3b036b29ea330e74c82e0' + '&output=json')
r2 = requests.get('http://www.opensecrets.org/api/?method=candIndustry&cid=N00002221&cycle=2016&apikey=806206d71fc3b036b29ea330e74c82e0&output=json')
data2 = r2.json()
print data2
