 
# # task 6-------------------
import json
from bs4 import BeautifulSoup
with open ("task_5th.json","r")as f:
    data=json.load(f)
def analyse_movie_language(data):
    dict1={}
    for i in data:
        
        for j in i['language']:
            if j not in dict1:
                dict1[j]=1
            else:
                dict1[j]+=1
     
    with open("task6.json","w")as f:
        json.dump(dict1,f,indent=4)
analyse_movie_language(data)
 
     
     
