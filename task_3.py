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