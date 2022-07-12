import requests
import time
from bs4 import BeautifulSoup as bs
import csv

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

# ADRESE = "https://www.latloto.lv/lv/rezultati/superbingo/"

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

# html = """<div class="section-heading-page">
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

from bs4 import BeautifulSoup
def info(htmlDatne):
    with open(htmlDatne, "r", encoding="utf-8") as fails:
        html = fails.read()

    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all(div_class_ = "1. Centrs")

info("Superbingo/Lapas/lapa_1.html")