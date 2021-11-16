#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# import ssl
# from elasticsearch.connection import create_ssl_context
# from elasticsearch import Elasticsearch
# import urllib3
# from decouple import config
# import os
import itertools
import sys


# In[2]:


# ssl_context = create_ssl_context()
# ssl_context.check_hostname = False
# ssl_context.verify_mode = ssl.CERT_NONE


# In[3]:


# ELASTIC_HOST=config('ELASTIC_HOST')
# if ELASTIC_HOST == None:
#     ELASTIC_HOST='http://localhost'
# ELASTIC_PORT=config('ELASTIC_PORT')
# if ELASTIC_PORT == None:
#     ELASTIC_PORT=9200
# else:
#     ELASTIC_PORT=int(ELASTIC_PORT)
# ELASTIC_USER=config('ELASTIC_USER')
# if ELASTIC_USER == None:
#     ELASTIC_USER='user'
# ELASTIC_KEY=config('ELASTIC_KEY')
# if ELASTIC_KEY == None:
#     ELASTIC_KEY='123'


# In[4]:



# ELASTIC_HOST=os.getenv('ELASTIC_HOST')
# if ELASTIC_HOST == None:
#     ELASTIC_HOST='http://localhost'
# ELASTIC_PORT=os.getenv('ELASTIC_PORT')
# if ELASTIC_PORT == None:
#     ELASTIC_PORT=9200
# else:
#     ELASTIC_PORT=int(ELASTIC_PORT)
# ELASTIC_USER=os.getenv('ELASTIC_USER')
# if ELASTIC_USER == None:
#     ELASTIC_USER='user'
# ELASTIC_KEY=os.environ.get('ELASTIC_KEY')
# if ELASTIC_KEY == None:
#     ELASTIC_KEY='123'


# In[5]:



# print(ELASTIC_HOST)
# print(ELASTIC_PORT)
# print(ELASTIC_USER)
# print(ELASTIC_KEY)


# In[6]:


# es = Elasticsearch(hosts=[{'host': ELASTIC_HOST, 'port': ELASTIC_PORT}], scheme="http",verify_certs=False, timeout=300, ssl_context=ssl_context, http_auth=(ELASTIC_USER, ELASTIC_KEY))
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# In[7]:


# ######## 2020, 1 year ########
# ######## There are no MTM data in 2018, 2019 ########

# body = {
#          "size" : 100,
#          "query": {
#                  "range":{
#                     "TW_COLLECT_DT":{
#                         "gte":"2020-01-01T00:00:00.625+09:00",
#                         "lte":"2020-12-31T00:00:00.625+09:00" ################
#                     }
#                 }
#                  },
#     "sort":[{
#         "_id":"asc"
#     }]
# }
        
# res = es.search(index = 'd-2k-r-sago-temp', body=body)
# data = res['hits']['hits']
# # nxt=res["hit"]["hit"][-1]["sort"][0]
# total = res['hits']['total']

# # print(total)

# accident = []
# for da in data:
#     att_type = da['_source']
#     # att_type["POL_NM"]=att_type["SCEN_INFOS"][0]["POL_NM"]
#     accident.append(att_type)

# # df = pd.DataFrame(accident,dtype=str)
# df_10000 = pd.DataFrame(accident)

# print(df_10000.head())


# In[8]:


output=[]
for i in itertools.count(5,5):
    if i==35:
        break
    else:
        print(i,end=' ')
    output.append(i)
print(output)


# In[9]:


# print(j)


# In[10]:



 
file_path = './result/output.txt'
sys.stdout = open(file_path, "w")
print(output)


# In[ ]:




