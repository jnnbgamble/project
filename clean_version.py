import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#List of all industry codes
industry_pull = pd.read_csv('data/all_industries.txt', sep='\t')
all_industry_codes = industry_pull[['Catorder', 'Industry']].drop_duplicates()
all_industry_codes = all_industry_codes.set_index('Catorder')

#List of all congressional committees
all_committee_codes = pd.read_csv('data/all_committees.txt', sep='\t')


def getCommitteeData(congress_year, committee_code, industry_code):
    #Build API query string
    congress_year = str(congress_year)
    tob_ag = 'https://www.opensecrets.org/api/?method=congCmteIndus&congno=' + congress_year + '&indus=' + industry_code + '&cmte=' + committee_code + '&apikey=806206d71fc3b036b29ea330e74c82e0'
    r = requests.get(tob_ag + '&output=json')
    tob_ag = r.json()
    
    #list of dictionaries
    tob_ag['response']['committee']['member'][1]['@attributes']
    len(tob_ag['response']['committee']['member'][1]['@attributes'])
    
    #The below code takes all the important values from the API output, builds it into a list of lists, and deposits 
    #it into a dataframe
    committee_list = []
    
    for x in range(len(tob_ag['response']['committee']['member'])):
        member_values = [tob_ag['response']['committee']['member'][x]['@attributes']['member_name'], 
                         tob_ag['response']['committee']['member'][x]['@attributes']['party'],
                         tob_ag['response']['committee']['member'][x]['@attributes']['state'],
                         tob_ag['response']['committee']['member'][x]['@attributes']['total'],
                         tob_ag['response']['committee']['member'][x]['@attributes']['indivs'],
                         tob_ag['response']['committee']['member'][x]['@attributes']['pacs']]
        committee_list.append(member_values)
        
    cols = ['member_name', 'party', 'state', 'total', 'indivs', 'pacs']
    committee = pd.DataFrame(committee_list, columns=cols)
    
    #Displays total contributions to committee, individual contributions, pac contributions, and a graph of contributions
    #by congressperson 
    print str(committee.total.astype(int).sum()) + ' : Total dollars donated to this committee'
    print str(committee.indivs.astype(int).sum()) + ' : Individual contributions' 
    print str(committee.pacs.astype(int).sum()) + ' : Pac contributions'
    print str(committee.party.value_counts())
    
    #Graphs committee contributions 
    values = committee[['indivs', 'pacs']].astype(int)
    #names = committee['member_name'].tolist()
    values.plot(kind='bar', stacked=True)
    plt.xlabel('Congressperson')
    plt.ylabel('Dollars donated')
    plt.title('Industry: ' + all_industry_codes.get_value(industry_code, 'Industry') + '      Committee: ' + all_committee_codes.get_value(committee_code, 'code   cmtename')) #Here I need to add the committee name
    #plt.xticks(values, names, rotation='vertical') Have to get this to display the congressperson's name vertically
    plt.show()
    return committee, all_industry_codes.get_value(industry_code, 'Industry')


#Get data for many committees
#for i in range(len(all_industry_codes)):
#    print i

def getCongresspersonBills(congress_year, industry):
    bill_query = 'https://www.govtrack.us/api/v2/bill?q=' + industry + '&congress=' + str(congress_year) + '&limit=500'
    
    print bill_query
    #Get all bills for that search query
    #Build up list of all bill IDs
    #Get cosponsors of bills 
    
    
x, y = getCommitteeData(114, 'HAGR', 'A06')
getCongresspersonBills(114, 'Dairy')


#Return bills in this congress for all members of that committee

