



# """
   
# Python’da kütüphaneleri kullanmanın en temel yolu import ifadesidir.

# Örnek: math kütüphanesi

# import math

# print(math.sqrt(16))  # 16'nın karekökü -> 4.0
# print(math.pi)        # pi sayısı -> 3.141592653589793

# Burada math kütüphanesini programına dahil ettik ve içindeki sqrt fonksiyonunu kullandık.     
      
# Sadece belli bir fonksiyonu/modülü import etmek

# Bazen bütün kütüphaneyi eklemek yerine sadece bir kısmını eklemek isteyebilirsin.

# from math import sqrt, pi

# print(sqrt(25))  # 25'in karekökü -> 5.0
# print(pi)        # pi sayısı

# Kütüphaneyi kısa bir isimle kullanmak

# Büyük kütüphaneler uzun isimli olabilir. as ile kısa isim verebilirsin.

# import numpy as np

# arr = np.array([1, 2, 3])
# print(arr)

# Python kütüphanelerini yüklemek

# Python’un standart kütüphaneleri zaten yüklü gelir (math, datetime, random vb.).
# Ama dışarıdan kütüphane kullanacaksan, önce yüklemen gerekir:

# pip install requests

# Sonra programında kullanabilirsin:

# import requests

# response = requests.get("https://www.example.com")
# print(response.status_code)

# ---

# Özet:

# import kütüphane_adı → tüm kütüphaneyi kullan.

# from kütüphane_adı import fonksiyon → sadece istediğin fonksiyonu kullan.

# import kütüphane_adı as kısaisim → kısa isimle kullan.

# Dış kütüphane gerekiyorsa pip install kütüphane_adı.

# En çok kullanılan kütüphanler
# matematik
# -random
# -math
# -numpy(hızlımsayısal hesaplamalar,matris,büyükveridizileri)

# Veri işleme analiz
# -pandas(tablo ve veri çerçeveleri(dateframe),veriokuma,yazma)
# -openpyxl (exel dosyası okuma yazma)
# csv(csv dosyalarını okuma,yazma(standart kütüphane))

# Web ve İnternet İşlemleri kütüphane	
# requests	Web sayfalarına istek gönderme (GET/POST)
# beautifulsoup4	HTML ve XML verilerini parsing / çekme
# selenium	Tarayıcı otomasyonu, web scraping

# Örnek:

# import requests
# response = requests.get("https://www.example.com")
# print(response.status_code)

# ---

# Görselleştirme ve Grafik Kütüphane	Kullanım Alanı

# matplotlib	Grafik çizme, veri görselleştirme
# seaborn	İstatistiksel grafikler, matplotlib’in üstünde kolay kullanım
# plotly	Etkileşimli grafikler ve tablolar

# Örnek:

# import matplotlib.pyplot as plt

# x = [1,2,3]
# y = [10,20,30]
# plt.plot(x,y)
# plt.show()

# ---

# Tarih, Saat ve Sistem İşlemleri Kütüphane	Kullanım Alanı
# datetime	Tarih ve saat işlemleri
# time	Programı duraklatma, zaman ölçme
# os	Dosya ve sistem işlemleri, klasör yönetimi

# Örnek:

# import datetime
# now = datetime.datetime.now()
# print(now)

# import os

# """



#odev3
import random
sayi=random.randint(1,100)
print(sayi)


hak=int(input("sayıyı kaç seferde tahmin edeceksiniz: "))
puan=100 #100 üzerinden her bir soru 20 puan

for i in range(1,hak+1,+1):
    tahmin= int(input("sayıyı tahmin ediniz: "))
    
    if(sayi==tahmin):
        print(f"{i}. seferde, bildiniz.")
        if(i<6):
            print(f"Puanınız: {puan-(20*(hak-i))}")
        else:
            print(f"Puan alamadınız.")
        break
    else:
       if(tahmin>sayi):
           print(f"{i}. tahmindesiniz.sayıyı daha küçük giriniz")
       else:
           print(f"{i}. Tahmindesiniz. sayı daha büyük giriniz")





##-------------------------------------------------------------------------------------------------------------------
# SORU2)Soru: Girilen bir sayının asal olup olmadığını bulun.
# **Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.

sayi=int(input("Asal sayı kontrolü için sayi giriniz: "))
if(sayi<2):
    print("Asal değildir")
elif(sayi==2):
    print("2 asaldır.")
else:
    for i in range(2,sayi):
        if(sayi%i==0):
            print(f"{sayi} asal değildir.")
            break
    else:
        print(f"{sayi} asaldır.")

# #________________________________________________________________________________________

# # """
# # Breakpoint koymak / kaldırmak: F9

# # Başlat (Debug): F5

# # Satır satır ilerle: F10

# # Fonksiyon içine gir: F11
# # """
# #------------------------------------------------------------------------
# # SORU)3
# # 3.1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
# # 3.2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonks
# # 3.3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
# # 3.4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür

#3.1

kez=int(input("Kelime kaç defa yazılsın: "))
kelime=input("Kelimeyi yazınz: ")
for i in range(0,kez+1):
   print(kelime)
#----------------------------------------------------------------------------------

#3.2
def listeyeCevir(*params):  ## * tek yıldızda tuple tipi liste ** çift yıldızda dictionary belirttiğimiz anlamına gelir
    liste1=[]
    liste1.append(params)
    print(liste1)

listeyeCevir(1,2,3)


##----------------------------------------------------------------------------------
#3.3
def AsalKontrol():
    sayi1=int(input("1. sayıyı giriniz: "))
    sayi2=int(input("2. sayıyı giriniz: "))
    if(sayi1>sayi2):
        # temp=sayi2 #temp ile
        # sayi2=sayi1
        # sayi1=temp
        sayi1,sayi2=sayi2,sayi1  # pythonda atama yapmanın kısa yolu
        print(sayi1,sayi2)
    if(sayi1<2):
        sayi1=2
    for j in range(sayi1,sayi2+1): 
        for i in range(2,j):
            if(j%i==0):
                # print(f"{j} asal değildir.")
                break
        else:
            print(f"{j} asaldır.")
    
AsalKontrol()
#----------------------------------------------------------
##3.4  Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür
sayi=int(input("sayı girin: "))
print(f'{sayi} sayısının tam bölenleri: ')
for i in range(sayi,0,-1):
    if(sayi%i==0):
        print(f'{i}' , end=" ")

# #Çok satırlı string istersen üçlü tırnak da kullanabilirsin:
# print("""Merhaba
# Dünya
# Python""")

