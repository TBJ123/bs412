#!/usr/bin/env python
# coding: utf-8

# In[35]:


from bs4 import BeautifulSoup
import requests
url = 'https://www.chinatimes.com/?chdtv'
html = requests.get(url)
soup = BeautifulSoup(html.text,'lxml')
titles = soup.find_all('section','hot-news')

for title in titles:
    a_tag = title.find_all('a')
    for tag in a_tag:
        a_href = tag.get('href')
        print(tag.text+'\n'+"網址: "+a_href)
        print('\n')
        
    
    
    


# In[ ]:




