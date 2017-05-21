import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tob_ag = 'https://www.opensecrets.org/api/?method=congCmteIndus&congno=114&indus=A02&cmte=HAGR&apikey=806206d71fc3b036b29ea330e74c82e0'
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
plt.title('Tobacco and the House Agriculture Committee')
#plt.xticks(values, names, rotation='vertical') Have to get this to display the congressperson's name vertically
plt.show()





committee_bar = committee['pacs'].astype(int)
#committee_bar.plot.bar(stacked=True) 
#NEXT TASK: SET AXIS TO NAMES OF CONGRESSPEOPLE



