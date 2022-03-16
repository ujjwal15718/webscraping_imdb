
# import requests
# from bs4 import BeautifulSoup
# import json
# user=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
# data=BeautifulSoup(user.text,"html.parser")
# def moviedata():
#     list=[]
#     mainDiv=data.find("div",class_="body_main container")

#     subDiv=mainDiv.find("table",class_="table")

#     tableall=subDiv.find_all('tr')

#     for i in tableall:
#         alltds=i.find_all('td')
#         d={}
#         for j in alltds:
#             rank=i.find('td',class_="bold").get_text()[:-1]
#             d["rank"]=int(rank)

#             rating=i.find("span",class_="tMeterScore").get_text()[1:3]
#             d["rating"]=int(rating)

#             review=i.find("td",class_="right hidden-xs").get_text()
#             d["review"]=int(review)

#             movieName=i.find("a",class_="unstyled articleLink")["href"][3:]
#             d["movieName"]=movieName

#             movieurl=i.find("a",class_="unstyled articleLink")["href"]
#             m="https://www.rottentomatoes.com"+movieurl
#             d["movieurl"]=m

#             Year=i.find('a',class_="unstyled articleLink").text

#             d["Year"]=int(Year[-5:-1])

#         list.append(d.copy())
#         if {} in list:
#             list.remove({})
#     with open("task1.json","w+") as file:
#         json.dump(list,file,indent=4)
#     return list
# moviedata() 




# import requests
# from bs4 import BeautifulSoup
# import json
# file=open("task1.json")
# movies=json.load(file)
# def group_by_year():
#     d={}
#     for i in movies:
#         movie_list=[]
#         year=i["Year"]
#         if year not in d:
#             for j in movies:
#                 if year==j["Year"]:
#                     movie_list.append(j)
#             d[year]=movie_list
#     with open ("task2.json","w+") as file1:
#         json.dump(d,file1,indent=4)
#         a=json.dumps(d)
# group_by_year()








 
# import requests 
# from bs4 import BeautifulSoup
# import json
# from pprint import pprint
 
# url= "https://www.imdb.com/india/top-rated-indian-movies/"
# page=requests.get(url)
# soup=BeautifulSoup(page.text,'html.parser')
# def scrap_top_list():
#     main_div=soup.find('div',class_='lister')
#     tbody=main_div.find('tbody',class_='lister-list')
#     trs=tbody.find_all('tr')

#     movie_name=[]
#     movie_rank=[]
#     movie_rating=[]
#     year_of_realese=[]
#     movie_url=[]

#     for tr in trs:
#         position=tr.find('td',class_="titleColumn").get_text().strip()
#         rank=''
#         for i in position:
#             if "." not in i:
#                 rank+=i
#             else:
#                 break
#         movie_rank.append(rank)
  
 
#         title=tr.find('td',class_="titleColumn").a.get_text()
#         movie_name.append(title)

#         year=tr.find('td',class_="titleColumn").span.get_text()
#         year_of_realese.append(year)

#         imdb_rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
#         movie_rating.append(imdb_rating)

#         link=tr.find('td', class_="titleColumn").a['href']
#         movie_link="https://www.imdb.com"+link
#         movie_url.append(movie_link)

#     Top_movies=[]
#     details={'position':'','name':'','year':'','rating':'','url':''}
#     for i in range(0,len(movie_rank)):
#         details['position']=int(movie_rank[i])
#         details['name']=str(movie_name[i])
#         year_of_realese[i]=year_of_realese[i][1:5]
#         details['year']=int(year_of_realese[i])
#         details['rating']=float(movie_rating[i])
#         details['url']=movie_url[i]
#         Top_movies.append(details.copy())
#         details={'position':'','name':'','year':'','rating':'','url':''}
#     with open ("store.json","w+") as file1:
#         json.dump(Top_movies,file1,indent=4)
#         a=json.dumps(Top_movies)
     
#     return(Top_movies)

# pprint(scrap_top_list())

 

 




# import requests
# from bs4 import BeautifulSoup
# import json
# url="https://www.imdb.com/india/top-rated-indian-movies"
# data=BeautifulSoup(url.text,"html.parser")
# def group_by_year(movies):

    
 

# ----------------------------------------------------------------------------------------------------------

 


# #  ----------task_2------------------------
# import requests
# from bs4 import BeautifulSoup
# import json
# file=open("store.json")
# movies=json.load(file)
# def group_by_year():
#     Top_movies={}
#     for i in movies:
#         movie_list=[]
#         year=i["year"]
#         if year not in Top_movies:
#             for j in movies:
#                 if year==j["year"]:
#                     movie_list.append(j)
#             Top_movies[year]=movie_list
#     with open ("store_2.json","w+") as file1:
#         json.dump(Top_movies,file1,indent=4)
#         a=json.dumps(Top_movies)
# group_by_year()


# --------------task_3------------------------------
# import requests,json
# from bs4 import BeautifulSoup
# file_new=open("store.json")
# movies=json.load(file_new)
# decades_10_years={"1970":[],"1980":[],"1990":[],"2000":[],"2010":[],"2020":[],"2030":[]}
# def group_by_decades( movies):
#     for index in movies:
#         if index["year"]>=1970 and index["year"]<1980:
#             decades_10_years["1970"].append(index)
#         elif index["year"]>=1980 and index["year"]<1990:
#             decades_10_years["1980"].append(index)
#         elif index["year"]>1990 and index["year"]<2000:
#             decades_10_years["1990"].append(index)
#         elif index["year"]>2000 and index["year"]<2010:
#             decades_10_years["2000"].append(index)
#         elif index["year"]>2010 and index["year"]<2020:
#             decades_10_years["2010"].append(index)
       
#     with open("task_3.json","w+")as file3:
#         json.dump( decades_10_years,file3,indent=4)
#         a=json.dumps(decades_10_years)
# group_by_decades(movies)



 
    
# ---------------------T------A--------S---------K-----------4-----------------------------
#Task 4---------------------Task_4------------------------


# import requests,json
# from bs4 import BeautifulSoup
# movie_url="https://www.imdb.com/title/tt15097216/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=ZAD0S85PKQMP6QYQX5M7&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_1"
# movie_name="Jai_Bhim"
# def scrape_movie_details(movie_name,movie_url):
    # url=requests.get(movie_url)
    # data=BeautifulSoup(url.text,"html.parser")
    # main_div=data.find('div',class_="TitleBlock__SeriesParentLinkWrapper-sc-1nlhx7j-3 itQvtY").h1.get_text()
    # print(main_div)
# scrape_movie_details(movie_name,movie_url)

    
# import requests,json
# from bs4 import BeautifulSoup

# def scrape_movie():
#     url="https://www.imdb.com/title/tt8176054/"
#     re=requests.get(url)
#     soup=BeautifulSoup(re.text,'html.parser')
    
#     movi_name=soup.find('div',class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt").h1.get_text()
#     movie_name=movi_name


#     return movi_name



 




















# import requests
# from bs4 import BeautifulSoup
# import json
# movieurl="https://www.rottentomatoes.com/m/toy_story_4"
# movieName="toy_story_4"
# def scrape_movie_details(movieName,movieurl):
#     url=requests.get(movieurl)
#     data=BeautifulSoup(url.text,"html.parser")
#     main_div=data.find_all("li",class_="meta-row clearfix")
#     dic={}
#     for i in main_div:
#         var=i.text
#         ng=var.split(":")
#         if "\nRating" in ng:
#             dic["Rating"]= ng[1].replace("\n","").strip()
#         elif "\nGenre" in ng:
#             gen=ng[1].replace("\n                        ","").strip()
#             list1=[]
#             s=""
#             for i in gen:
#                 if i==",":
#                     list1.append(s)
#                     s=""
#                 else:
#                     s+=i                
#             dic["Genre"]=list1
#         elif "\nOriginal Language" in ng:
#             dic["language"]=ng[1].replace("\n","").strip()
#         elif "\nDirector" in ng:
#             i=0
#             list2=[]
#             while i <len(ng):
#                 if i==0:
#                     i+=1
#                     continue
#                 list2.append(ng[i].replace("\n",""))
#                 i+=1
#             add=""
#             for s in list2:
#                 for s2 in s:
#                     if s2==" ":
#                         continue
#                     else:
#                         add+=s2
#             list5=add.split(",")
#             dic["director"]=list5
#         elif "\nProducer" in ng:
#             i=0
#             list3=[]
#             while i <len(ng):
#                 if i==0:
#                     i+=1
#                     continue
#                 list3.append(ng[i].replace("\n                        ","").strip())
#                 i+=1
#             add=""
#             for k in list3:
#                 for eachC in k:
#                     if eachC==" ":
#                         continue
#                     else:
#                         add+=eachC
#             list4=add.split(",")
#             dic["Producer"]=list4
#         elif "\nRuntime" in ng:
#             s=ng[1].replace("\n","").strip()
#             h=int(s[0])*60
#             i=0
#             j=" "
#             while i<len(s):
#                 if s[i]=="h" or s[i]=="m"  or s[i]==" " or i==0 or s[i]=="M":
#                     i+=1
#                     continue
#                 else:
#                     j+=s[i]
#                     i+=1
#                 h+=int(j)
#             dic["Runtime"]=h
#             dic["movieName"]=movieName                
#     with open("task4.json","w+") as file4:
#             json.dump(dic,file4,indent=4)
#             a=json.dumps(dic)
#             return dic
# scrape_movie_details("toy_story_4","https://www.rottentomatoes.com/m/toy_story_4")



import json
from bs4 import BeautifulSoup
with open ("task_5th.json","r")as f:
    data=json.load(f)
def analyse_movie_language(data):
    dict1={}
    for i in data:
        if tuple(i['language']) not in dict1:
            dict1[tuple(i['language'])]=1
        else:
            dict1[tuple(i['language'])]+=1
    print(dict1)

    #     for j in i['language']:
    #         if j not in dict1:
    #             dict1[j]=1
    #         else:
    #             dict1[j]+=1
    # # # print(dict1)
    # with open("task6.json","w")as f:
    #     json.dump(dict1,f,indent=4)
analyse_movie_language(data)
 
     
     
