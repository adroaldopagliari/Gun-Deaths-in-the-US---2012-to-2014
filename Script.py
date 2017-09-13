
# coding: utf-8

# In[22]:


import csv
f = open('guns.csv', 'r')
data = list(csv.reader(f))


# In[23]:


print(data[:5])


# In[24]:


headers = data[:1]
headers


# In[27]:


data = data[1:]


# In[28]:


data[:5]


# In[31]:


years = [x[1] for x in data]
years


# In[32]:


year_counts = {}

for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1
        
year_counts


# In[40]:


import datetime
dates = [datetime.datetime(year=int(x[1]),month=int(x[2]),day=1) for x in data]


# In[42]:


dates[0:4]


# In[44]:



date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 0
    date_counts[date] += 1

date_counts


# In[46]:


sex_counts = {}

for row in data:
    if row[5] not in sex_counts:
        sex_counts[row[5]] = 0
    sex_counts[row[5]] += 1
sex_counts


# In[47]:


race_counts = {}

for row in data:
    if row[7] not in race_counts:
        race_counts[row[7]] = 0
    race_counts[row[7]] += 1
race_counts


# Data facts: The most part of gun deaths involve men of white race. The minorities are'nt so affect by these possible crimes, but we need to verify the intents of crimes. Another data must be considered further: season.

# In[53]:


with open('census.csv', 'r') as f:
    census = list(csv.reader(f))
census


# In[54]:


race_counts


# In[55]:


mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}


# In[56]:


race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# In[57]:


intents = [x[3] for x in data]
intents


# In[58]:


races = [x[7] for x in data]
races


# In[60]:


homicide_race_counts = {}
for i,race in enumerate(races):
    if intents[i] == 'Homicide':
        if race not in homicide_race_counts:
            homicide_race_counts[race] = 1
        else:
            homicide_race_counts[race] += 1
homicide_race_counts
    


# In[61]:


race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# Despite of the most part of guns deaths was associated to white men, when we only consider homicides its evident that there is a correlation among black people and these deaths, the same for hispanics.
# 
# In future we need to verify if there's a correlation between other intents and races and between other variables with races and intents.
