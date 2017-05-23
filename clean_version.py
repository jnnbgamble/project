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

#
all_congress_ids = pd.read_csv('data/legislators-current.csv')
all_congress_ids = all_congress_ids[['last_name', 'first_name', 'bioguide_id', 'opensecrets_id', 'govtrack_id']]


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


#This gives you your list of bills that match the search term
def getCongresspersonBills(congress_year, industry): #CHANGE LIMIT LATER
    bill_query = 'https://www.govtrack.us/api/v2/bill?q=' + industry + '&congress=' + str(congress_year) + '&limit=4'
    print bill_query
    r2 = requests.get(bill_query)
    output = r2.json()
    
    bill_id_list = []
    bill_sponsors_cosponsors = {}
    id_to_scs = {}
    
    #Builds a list of bill IDs for the proper query string
    for x in range(len(output['objects'])): 
        bill_id_list.append(output['objects'][x]['id'])
    #print bill_id_list
    
    #For each bill ID, builds a list of sponsors and cosponsors 
    for x in range(len(bill_id_list)):
        bill_query = 'https://www.govtrack.us/api/v2/bill/' + str(bill_id_list[x])
        r3 = requests.get(bill_query)
        relevant_bills = r3.json()
        
        sponsor = relevant_bills['sponsor']['bioguideid']
        cosponsors = []
        for y in range(len(relevant_bills['cosponsors'])):
            cosponsors.append(relevant_bills['cosponsors'][y]['bioguideid'])
        #print str(cosponsors)
        #Builds bill ID : sponsors & cosponsors dictionary
        bill_sponsors_cosponsors['sponsor'] = sponsor
        bill_sponsors_cosponsors['cosponsors'] = cosponsors
        #print 'bill_sponsors_cosponsors: ' + str(bill_sponsors_cosponsors)
        #print 'ID to SCS : ' + str(id_to_scs)
        id_to_scs[str(bill_id_list[x])] = bill_sponsors_cosponsors
        #print x
        #print bill_sponsors_cosponsors
        print id_to_scs[str(bill_id_list[x])]

    for x in range(len(bill_id_list)):
        id_to_scs[]           
    return id_to_scs


#Describtion
#def fundingPersonComparison():
#sns.heatmap()


test_dict = getCongresspersonBills(114, 'Dairy')    
committee_df, industry = getCommitteeData(114, 'HAGR', 'A06')
print test_dict