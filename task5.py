# task_5
import json,requests
from task_4 import scrape_movie
from pprint import pprint
with open("task_1.json")as u:
    data=json.load(u)
def get_movie_list_details():
    for i in data[:20]:
        url1=i["url"]
        link3 = scrape_movie(url1)
        # pprint(link3)
    # with open("task5_new.json","w+")as f:
    #     json.dump(link3,f,indent=4)
    return link3
# get_movie_list_details()
# print("successful")