# task_8
import json,requests
from pprint import pprint
with open("task_1.json","r")as f:
    x=json.load(f)
def scrape_movie_details_url():
    l=[]
    for i in x :
        store_url=i['url']
        result=(store_url[27:36])
        l.append(result)
         
    with open("task8.json","w")as file:
        json.dump(l,file ,indent=5)         
            
scrape_movie_details_url()
