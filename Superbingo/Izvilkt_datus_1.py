from cgitb import html
import requests
import time
from bs4 import BeautifulSoup as bs
import csv

def info(htmlDatne):
    with open(htmlDatne, "r", encoding="utf-8") as f:
        html = f.read()

    zupa = bs(html, "html.parser")

    cipari = zupa.find_all("div", class_ ="numbered-items numbered-items-purple margin-bottom-5")
    
    for saraksts in cipari:
        print(saraksts)
    

info("Superbingo/Lapas/lapa_1.html")
info("Superbingo/Lapas/lapa_2.html")
info("Superbingo/Lapas/lapa_3.html")
info("Superbingo/Lapas/lapa_4.html")
info("Superbingo/Lapas/lapa_5.html")
info("Superbingo/Lapas/lapa_6.html")
info("Superbingo/Lapas/lapa_7.html")
info("Superbingo/Lapas/lapa_8.html")
info("Superbingo/Lapas/lapa_9.html")
info("Superbingo/Lapas/lapa_10.html")