# from ast import Num
# from cgi import print_arguments
# from cgitb import html
# from numpy import append
# import requests
# import time
# from bs4 import BeautifulSoup as bs
# import csv
# import os,sys
# import subprocess
# import glob
# from os import path

# print("=================================")

# ADRESE = "https://www.latloto.lv/lv/rezultati/superbingo/1147512"

# def saglabat_lapu(adrese, fails):
#     pieprasijums = requests.get(adrese)

#     if pieprasijums.status_code == 200:
#         lapa = pieprasijums.text

#         with open(fails, "w", encoding="utf-8") as f:
#             f.write(lapa)

#     else:
#         print("radās kļūda", pieprasijums.status_code)
#         return

# saglabat_lapu(ADRESE, "Superbingo/Lapas/lapa_10.html") 

# print("=================================")

# import requests
# import time

# ADRESE = "https://www.latloto.lv/lv/rezultati/superbingo/1147530"

# def atvilkt_lapas(daudzums):
#     for i in range(1147530, daudzums - 2):
#         adrese = f"{ADRESE}page{i}.html"
#         fails = f"Superbingo/lapas/lapa_{i}.html"

#         print("Pieprasijums uz", adrese, "--->.",  fails)
#         saglabat_lapu(adrese, fails)

#         time.sleep(2)

# atvilkt_lapas(10)

# print("=================================")

# def info(htmlDatne):
#     with open(htmlDatne, "r", encoding="utf-8") as fails:
#         html = fails.read()

#     zupa = bs(html, "html.parser")

#     tabulas = zupa.find_all("Izloze Nr. 322764")
 
#     for tabula in tabulas:
#         print (tabula)
#         print("=================================")
#         print("=================================")
#         print("=================================")
#         print("=================================")
#         print("=================================")
#         print("=================================")

#     print(zupa)
# print("=================================")
#     tabulas = zupa.find

        # print(html)

# from bs4 import BeautifulSoup

#  print("=================================")

# html = """<div class="numbered-items numbered-items-purple margin-bottom-5">
#   <div class="container">
    
#   </div>
# </div>
# <div class="container"><p>Hello 1</p><p>Hello 2</p></div>"""

# soup = BeautifulSoup(html, 'html.parser')
# div_2 = soup.find_all('div', attrs={'class': 'container'})[1]

# for p in div_2.find_all("p"):
#     print(p.text)    # Display the text inside any p tag

# info("Superbingo/Lapas/lapa_1.html")

#  print("=================================")

# from bs4 import BeautifulSoup

# def info(htmlDatne):
#     with open(htmlDatne, "r", encoding="utf-8") as fails:
#         html = fails.read()

#         soup = BeautifulSoup(html, "html.parser")
#         elements = soup.find_all (div class = "numbered-items-purple margin-bottom-5")
    
#     print(fails.read)


# info("Superbingo/Lapas/lapa_1.html")

# def info(htmlDatne):
#     with open(htmlDatne, "r", encoding="utf-8") as f:
#         html = f.read()

#     zupa = bs(html, "html.parser")

#     cipari = zupa.find_all("div", class_ ="numbered-items numbered-items-purple margin-bottom-5")
    
#     for saraksts in cipari:
#         print(saraksts)

# info("Superbingo/Lapas/lapa_1.html")
# info("Superbingo/Lapas/lapa_2.html")
# info("Superbingo/Lapas/lapa_3.html")
# info("Superbingo/Lapas/lapa_4.html")
# info("Superbingo/Lapas/lapa_5.html")
# info("Superbingo/Lapas/lapa_6.html")
# info("Superbingo/Lapas/lapa_7.html")
# info("Superbingo/Lapas/lapa_8.html")
# info("Superbingo/Lapas/lapa_9.html")
# info("Superbingo/Lapas/lapa_10.html")


# for saraksts in cipari:

# interval_1_16++;

# sys.stdout = open('output.txt','w')
# print (saraksts)
# sys.stdout.close()
    # sys.stdout = open('output.csv','w')
    # append (saraksts.output.csv)
    

    # sys.stdout.close()    # sys.stdout = open('output.csv','w')
        
    # return cipari 
    # sys.stdout.close()

    