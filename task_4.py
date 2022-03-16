# task_4
import requests,json
from bs4 import BeautifulSoup
from pprint import pprint
director_list=[]
def scrape_movie(url):
    re=requests.get(url)
    soup=BeautifulSoup(re.text,'html.parser') 
    
    movi_name=soup.find('div',class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt").h1.get_text()
    
 
    director = soup.find("li", class_="ipc-metadata-list__item")
    dire = director.findAll("a")
    l=[]
    for i in dire:
        l.append(i.text)
    # print(l)

    origin_of_country=soup.find('li',attrs={"data-testid":"title-details-origin"})
    country=origin_of_country.find('li',class_="ipc-inline-list__item").a.get_text()
     
    language=soup.find('li',attrs={"data-testid":"title-details-languages"})
    movie_language=language.ul
    lang_list = movie_language.find_all("li")
    langs = []
    for i in lang_list:
        langs.append(i.get_text())
    poster=soup.find('div',{"data-testid":"hero-media__poster"})
    poster_inside=poster.find('div',class_="ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img")
    poster_src_url=poster_inside.find('img',class_="ipc-image")["src"]
     
    
    Bio=soup.find("div", attrs={"data-testid":"storyline-plot-summary"})
    Bio_inside=Bio.find("div", class_="ipc-html-content ipc-html-content--base").div.text
    
    runtime=soup.find('li',attrs={"data-testid":"title-techspec_runtime"})
    run_inside=(runtime.div).text
    store_hour=(run_inside[:1])
    store_min=(run_inside[8:10])
    total_min=((int(store_hour)*60)+int(store_min))
    total_run_time=total_min

    Genere=soup.find('li',attrs={"data-testid":"storyline-genres"})
    genere_inside_div=Genere.find('div',class_="ipc-metadata-list-item__content-container")
    genere_inside_ul=genere_inside_div.find('ul',class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base") 
    genere_inside_li=genere_inside_ul.find('li',class_="ipc-inline-list__item")
    gen_re=[]
    for index in genere_inside_li:
        gen_re.append(index.get_text())

    dic = {'movie_name':movi_name, 'director':l, 'country_origin':country ,'language':langs,'url': poster_src_url,'bio':Bio_inside,'Time_duration':total_min,'genere_of_the_movie': gen_re}
    
    director_list.append(dic)
    return director_list

    # with open('task_4th.json',"w+")as file_task_4:
    #     json.dump( director_list,file_task_4,indent=4)
    
# scrape_movie("https://www.imdb.com/title/tt8176054/")


 
