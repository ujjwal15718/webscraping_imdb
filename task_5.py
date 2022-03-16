import json,requests
from bs4 import BeautifulSoup
       
def scrape_movie(url):
    
    re=requests.get(url)
    soup=BeautifulSoup(re.text,'html.parser') 
    
    movi_name=soup.find('div',class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt").h1.get_text()
    

    # director=soup.find('div', attrs={ "data-testid":"shoveler-items-container"})
    # director_in=director.find('div',class_="ipc-shoveler__arrow ipc-shoveler__arrow--visible ipc-shoveler__arrow--right ipc-pager ipc-pager--visible ipc-pager--right")
    # director_inside=director_in.find('svg',class_="ipc-icon ipc-icon--chevron-right-inline ipc-icon--inline ipc-pager-icon")
    # director_inside_2=director_inside.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-all StyledComponents__CastMetaDataList-sc-y9ygcu-12 dXTKrS ipc-metadata-list--base")
    # director_3=(director_inside_2.find('li',class_="ipc-metadata-list__item").find('span',class_="ipc-metadata-list-item__label"))
    # director_4=director_3.find('div',class_="ipc-metadata-list-item__content-container")
    # director_5=director_4.find('ul',class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base")
    # director_6=director_5.find('li',class_="ipc-inline-list__item")
    # director_7=director_6.find('a',class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")
    # final_director_list=[]
    # for final_director in director_7:
    #     final_director_list.append(final_director.get.text())
     

 
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

    dic = {'movie_name':movi_name, 'director':'director_list','language':langs, 'country_origin':country ,'url': poster_src_url,'bio':Bio_inside,'Time_duration':total_min,'genere_of_the_movie': gen_re}
  
     
    return dic
 
director_list_result=[]
count=1
with open("task_1.json","r")as f:
    data=json.load(f)
    for i in data[:10]:
        director_list_result.append(scrape_movie(i['url']))
        print("successful file - ",count)
        count+=1 
with open("task_5th.json","w")as file_5:
    json.dump(director_list_result,file_5, indent=4)


