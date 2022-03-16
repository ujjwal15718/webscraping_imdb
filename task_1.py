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
#     with open ("task_1.json","w+") as file1:
#         json.dump(Top_movies,file1,indent=4)
#         a=json.dumps(Top_movies)
     
#     return(Top_movies)

# pprint(scrap_top_list())
