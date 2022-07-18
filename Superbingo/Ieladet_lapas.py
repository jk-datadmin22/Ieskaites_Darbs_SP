from cgitb import html
import requests
import time
from bs4 import BeautifulSoup as bs
import csv



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

saglabat_lapu(ADRESE, "superbingo/Lapas/lapa_10.html")
