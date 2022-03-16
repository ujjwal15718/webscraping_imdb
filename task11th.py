# task_11------------------------------
import json
from pprint import pprint
with open("task_4th.json","r")as f:
    var=json.load(f)
dict2={}
def analyse_movies_genre ():
    for i in var:
        for g in  i['genere_of_the_movie']:
            if g in dict2:
                dict2[g]+=1
            else:
                dict2[g]=1
            
    print(dict2)
analyse_movies_genre ()

