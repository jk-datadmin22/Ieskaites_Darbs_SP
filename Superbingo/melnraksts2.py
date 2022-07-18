from ast import Num
from cgi import print_arguments
from cgitb import html
from numpy import append
import requests
import time
from bs4 import BeautifulSoup as bs
import csv
import os,sys
import subprocess
import glob
from os import path

def info(htmlDatne):
    with open(htmlDatne, "r", encoding="utf-8") as f:
        html = f.read()

    zupa = bs(html, "html.parser")

    cipari = zupa.find_all("div", class_ ="numbered-items numbered-items-purple margin-bottom-5")
    
    for saraksts in cipari:
        # print (saraksts)

    # skaitli =saraksts    
    # for skaitli in range(1, 75):
    #     print(skaitli)

        sys.stdout = open('output.csv','a')
        print(saraksts)
    
    # sys.stdout.close()
    

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



# sys.stdout.close()