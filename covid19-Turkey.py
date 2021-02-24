import requests
from bs4 import BeautifulSoup
import time
try:

    r = requests.get('https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html').content
    soup = BeautifulSoup(r, "html.parser")
    all_datas = soup.find_all("script")
    index = all_datas[18]
    index = str(index).split('"')
    test_sayisi = index[9]
    hasta_sayisi = index[17]
    vefat_sayisi = index[21]
    iyilesen_sayisi = index[25]
    riskli_hasta = index[57]
except:
    print("İnternet Bağlantınızda Sorun Var!")
    

while True:
    islem = input("Günlük korona virüs tablosunu görmek için ENTER\n Çıkış için 'q' -> ")

    if islem == "q":
        break

    else:
        try:
            print("\n◼  Bugünkü Test Sayısı:         {}".format(test_sayisi))
            print("◼  Vaka Sayısı:                 {}".format(hasta_sayisi))
            print("◼  Bugünkü Vefat Sayısı:        {}".format(vefat_sayisi))
            print("◼  Bugünkü İyileşen Sayısı:     {}".format(iyilesen_sayisi))
            print("◼  Ağır Hasta Sayısı:           {}\n".format(riskli_hasta))
        except:
            print("İnternet Bağlantınızda Sorun Var!")
