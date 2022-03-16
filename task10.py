#task_10
import json
from pprint import pp, pprint
from bs4 import BeautifulSoup
with open("task5_new.json","r")as f:
    data=json.load(f)
def analyse_language_and_directors(data):
    dic1={}
    for i in data:
       for dire in i['director']:
           if dire not in dic1:
               dic1[dire]={}
               for lang in i['language']:
                if lang not in dic1[dire].keys():
                    dic1[dire][lang]=1
                else:
                    dic1[dire][lang]+=1
    # pprint(dic1)
    with open("task10th.json","w+")as file10:
        json.dump(dic1,file10,indent=4)           
# analyse_language_and_directors(data)
 
