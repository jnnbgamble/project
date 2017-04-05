# Final Project

**What is the question you hope to answer?**
I want to be able to predict a politician's social media behavior based on their congressional voting record, sponsorship of bills, and committees they may be a part of. By "social media behavior" I mean things like: 
* The positivity/negativity of their tweets (categorical) 
* The percentage of their tweets that are heavily partisan
* The sorts of hashtags and other Twitter objects they're using to propagate their message
Example insights could include "congressmen that voted for X bill were Y% more likely to tweet negatively about the opposition party", "congressmen that vote republican 80% of the time are X% more/less likely to have a positive tweeting history", or "congressmen that included X hashtag in any tweets made them Y% more likely to have a very negative social media presence. 

(I've also considered doing a prediction the other way: can you predict a bill's likelihood to pass based on its social media presence and the social media behavior its sponsors and cosponsors? I'll make this decision once I've got a better handle on the data. 

**What data are you planning to use to answer that question?**
There are two datasets that I'm looking at joining. GovTrack, which is a service for tracking legislation in America, and Twitter, a social media platform that probably needs no explanation. Both have APIs that can be hooked into. 

**What do you know about the data so far?**
There's a C-SPAN list of congress people 562 members deep. There are 535 members of congress, so the first interesting quirk of the data is those extra 30 accounts. Twitter's documentation (https://www.brain.fm/app#!/player/35) allows for pulling tweets by a query and also has operators for things like hashtags. This will help identify particularly toxic/healthy hashtags and see if they have any predictive power. 

GovTrack's API allows for the pulling of data by bill, bill type (house resolution, house bill, senate resolution, etc.), sponsor/cosponsor, vote, committee, etc. The API (https://www.govtrack.us/developers/api) is very simple compared to Twitter's. 

**Why did you choose this topic?**
I chose this topic because politics is a passion of mine, and it will be interesting to take a social media behavior over time. It will also be interesting to see if hyper-partisan periods in history (like the one we're in now) result in a difference in the way legislation is passed.  
