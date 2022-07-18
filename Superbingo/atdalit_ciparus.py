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

# with open("output.csv", "r", encoding="utf-8") as f:
#     rindinas = f.readlines()
#     for rindina in rindinas:
#         print(rindina)
#     if rindina =(<span>19</span>)
#         print (rindina)

with open("output.txt",'r') as data_file:
    for line in data_file:
        data = line.split()
        print(data)


        # kolonas = rindina.split("<span>", int, "/span>\n")
        # print(kolonas)
        # SP1 = kolonas[1]
        # cip = float(kolonas[2])
        # SP2 = kolonas[3]
        #print(cip)
        # if klase == "3":
        #     summa = summa + cena
        #     skaits = skaits + 1
        #exit()