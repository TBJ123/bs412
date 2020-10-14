#!/usr/bin/env python
# coding: utf-8

# In[11]:


from bs4 import BeautifulSoup
import requests
url = 'https://dct.ntcu.edu.tw/news.php'
html = requests.get(url)
html.encoding='utf-8'
if html.status_code == requests.codes.ok:
    
    soup = BeautifulSoup(html.text,'lxml')
    print(soup)


# In[14]:


a_tag = soup.find_all('a')
for tag in a_tag:
    print('網址: '+tag.text+'->'+tag.get('href'))


# In[ ]:




