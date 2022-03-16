# task_7
import json,requests
with open("task5_new.json","r")as f:
    var=json.load(f)
def analyse_movies_directors():
    dict1={}
    for i in var:
        for j in i['director']:
            print(j)
            if j  in dict1:
                dict1[j]+=1
            else:
                dict1[j]=1
    print(dict1)
    # with open("task6.json","w")as f:
    #     json.dump(dict1,f,indent=4)
         
analyse_movies_directors()