#!/usr/bin/env python
# coding: utf-8

# In[1]:



from bs4 import BeautifulSoup
html_doc = '''<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>'''
soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())


# In[5]:


title_tag = soup.title
print(title_tag.text)


# In[7]:


a_tag = soup.find_all('a')
for tag in a_tag:
    print(tag.string)


# In[8]:


for tag in a_tag:
    print(tag.get('href'))


# In[ ]:




