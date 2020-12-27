#!/usr/bin/env python
# coding: utf-8

# # Salary.com Scraper

# Extract salary statistics based on job title and location criteria

# In[1]:


import re
import csv
import json
from time import sleep
from bs4 import BeautifulSoup
import requests


# In[2]:


template = 'https://www.salary.com/tools/salary-calculator/{}/{}'


# In[3]:


position = 'java-developer'
city = 'washington-dc'

url = template.format(position, city)

response = requests.get(url)


# In[4]:


soup = BeautifulSoup(response.text, 'html.parser')


# In[5]:


response.text


# In[47]:


import re
import csv
import json
from time import sleep
from bs4 import BeautifulSoup
import requests


# adding individual table data of a row to result
def extract_record(table_row):
    a = 0
    for td in table_row('td'):
        if(a == 0):
            percentile = td.text
            print(percentile)
        if(a == 1):
            salary = td.text
            print(salary)
        if(a == 2):
            location = td.text
            print(location)
        if(a == 3):
            last_updated = td.text
            print(last_updated)
            
        a = a + 1
        
    result = (percentile, salary, location, last_updated)
    return result

# main function to run
def main(position, location):
    
    template = 'https://www.salary.com/tools/salary-calculator/{}/{}'
    url = template.format(position, city)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    records = []
    
    # Adding table row data to records
    a = 5
    for tr in soup.find_all('tr'):
        if(a!=5):
            records.append(extract_record(tr))
        a = a - 1
        if(a==0):
            break
    
    # save data to csv file
    with open('salary.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Percentile', 'Salary', 'Location', 'Last Updated'])
        writer.writerows(records)
        
# run the main function
main('java-developer', 'los-angeles-ca')


# In[ ]:




