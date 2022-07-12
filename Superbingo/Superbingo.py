import requests
import time
from bs4 import BeautifulSoup as bs
import csv

# print("=================================")

ADRESE = "https://www.latloto.lv/lv/rezultati/superbingo/1147512"

def saglabat_lapu(adrese, fails):
    pieprasijums = requests.get(adrese)

    if pieprasijums.status_code == 200:
        lapa = pieprasijums.text

        with open(fails, "w", encoding="utf-8") as f:
            f.write(lapa)

    else:
        print("radās kļūda", pieprasijums.status_code)
        return

saglabat_lapu(ADRESE, "Superbingo/Lapas/lapa_10.html") 

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

def info(htmlDatne):
    with open(htmlDatne, "r", encoding="utf-8") as fails:
        html = fails.read()

    zupa = bs(html, "html.parser")

    tabulas = zupa.find_all("numbered-items numbered-items-purple margin-bottom-5")
 
    for tabula in tabulas:
        print (tabula)
        print("=================================")
        print("=================================")
        print("=================================")
        print("=================================")
        print("=================================")
        print("=================================")

    print(zupa)

#     tabulas = zupa.find

        # print(html)


info("Superbingo/Lapas/lapa_10.html") 