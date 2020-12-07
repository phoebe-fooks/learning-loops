#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = ['roads', 'cities', 'counties', 'states']


# In[2]:


my_empty_list = []


# In[3]:


for x in my_list:
    new_string = x + '.txt'
    my_empty_list.append(new_string)


# In[4]:


print (my_empty_list)


# In[5]:


import math


# In[6]:


x = math.pi
y = 0
while x <10000:
    x = math.pi**y
    y += 1
    print(x)

