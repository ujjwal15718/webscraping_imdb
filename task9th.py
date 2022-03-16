 
import random,json,time
from task_4 import scrape_movie
from os import path
from pprint import pprint
with open ("task_1.json","r")as file:
    url1=json.load(file)




def scrape_movie_json():
    time.sleep(random.randint(2,5))
    main_list = []
    for j in url1[:10]:
        url_name=j["url"]
        file_name=url_name[27:36]+".json"
        if path.exists(file_name):
            all_movie = json.load(open(file_name))
        else:
            all_movie= scrape_movie(url_name)
            with open(file_name,"w+") as f:
                json.dump(all_movie,f,indent=6)
        main_list.append(all_movie)
    return main_list
            
pprint(scrape_movie_json())
 
   


 
         