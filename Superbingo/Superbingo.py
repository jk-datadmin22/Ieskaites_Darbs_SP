import requests
import time

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

# eeeeeeeeee

# ADRESE = "https://www.latloto.lv/lv/rezultati/superbingo/"

# def atvilkt_lapas(daudzums):
#     for i in range(1, daudzums - 2):
#         adrese = f"{ADRESE}page{i}.html"
#         fails = f"Superbingo/lapas/lapa_{i}.html"

#         print("Pieprasijums uz", adrese, "--->.",  fails)
#         saglabat_lapu(adrese, fails)

#         time.sleep(2)

# atvilkt_lapas(10)

# def info(htmlDatne):
#     with open(htmlDatne, "r", encoding="utf-8") as fails:
#         html = fails.read()

#         print(html)

# def info(htmlDatne):
#     with open(htmlDatne, "r", encoding="utf-8") as fails:
#         html = fails.read()

#     zupa = bs(html, "html.parser")

#     tabulas = zupa.find



#         print(html)



# info("7diena/requests/lapas/lapa_1.html") 