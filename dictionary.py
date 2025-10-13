# key - value

# # 41 => koceli 34 => istanbul


# # {key : value}
# plakalar = {"kocaeli" : 41, "istanbul" : 34}

# plakalar["ankara"] = 6 #yeni key value eklemek.
# plakalar["kocaeli"] = "new value" #key valuesunu değiştirmek.

# users = {
#         "sadikduran" : {"age:" : 36,
#                         "email" : "
# sadik@gmail.com
# ",
#                         "roles" : ["user"],
#                         "adress" : "kocaeli",
#                         "phone" : "123213"},
#          "cinarturan" : {"age:" : 2,
#                         "email" : "
# cinar@gmail.com
# ",
#                         "roles" : ["admin", "user"],
#                         "adress" : "kocaeli",
#                         "phone" : "1223213"},}

# print(users["cinarturan"]) #cinarturanın bilgileri
# print(users["cinarturan"]["roles"]) #cinarturanın rol bilgileri







# ogrenciler={
#     '120': {
#         'ad': 'Ali',
#         'soyad': 'Yılmaz',
#         'telefon': '532 000 00 01'
#     },
#     '125': {
#         'ad': 'Alcan',
#         'soyad': 'Yılar',
#         'telefon': '532 000 00 02'
#     },
#     '128': {
#         'ad': 'Aliye',
#         'soyad': 'Yalaz',
#         'telefon': '532 000 00 03'
#     },
# }

#bilgileri verilen öğrenciler kullanıcıdan aldığınız bilgileri dicrionary içinde saklayınız
#öprenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin


# ogrenciler={
#     'No': {
#         'Ad': ''
#         'Soyad': ''
#         'telefon': ''
#         }
    
#     }
  






# ogrenciler = {}

# no=input("numara: ")
# isim=input("isim: ")
# soyisim=input("soyisim: ")
# telefon=input("telefon: ")

# ogrenciler={

#     '120': {
#         'ad': 'Ali',
#         'soyad': 'Yılmaz',
#         'telefon': '532 000 00 01'
#           }

#           }

# 


#
# Arabalar={}
# plaka
# isim
# soyisim
# phone

# Arabalar={}
# plaka=input("Plaka: ")
# ad=input("Adınız: ")
# soyad=input("Adınız: ")
# telefon=input("Telefon: ")
# Arabalar[plaka]={
#     "Ad": ad,
#     "Soyad":soyad,
#     "telefon":telefon,
# }
# print(Arabalar)
# plakaGiris=input("plaka giriniz:")
# print(Arabalar[plakaGiris])

# Arabalar[plaka]={"ad":ad, "soyad":soyad,"telefon":telefon}

#Öncelikle boş bir dictionary tanımlıyoruz   ----> Dictionar={}
# sonra kullanıcıdan input alıyoruz.Bu inputu bir değişkene atıyoruz. ---> no=input("isim girin: ")
#                                                                     ---> ad=input("no girin: ")
# Sonra boş tanımladığımız dictionary e  -----> Dictionay[no]{"ad":ad} diyerek alt küme ekliyoruz

# Bilet={}
# no=input("no:")
# ad=input("ad: ")
# soyad=input("Soyad ")
# koltuk=input("Koltuk No: ")
# Bilet.update({
#     no:{
#     "ad": ad,
#      "soyad":soyad,
#      "koltuk":koltuk
#     }
# })
# print(Bilet)
# biletNo=input("Bilet no girin: ")
# print(Bilet[biletNo])

aktorler={}
for i in range(1,4):
    adSoyad=input(f"{i}. Ad Soyad:")
    rol=input(f"{i}. Rolü:")
    dizi=input(f"{i}. dizi:")
    aktorler[i]={
    
    
        "Ad Soyad":adSoyad,
        "Rolü":rol,
        "Dizi":dizi
    }
print(aktorler)


ogrenciler = {}

for i in range(3):
    ad = input(f"{i+1}. öğrencinin adını girin: ")
    yas = input(f"{i+1}. öğrencinin yaşını girin: ")
    
    # update ile ekleme
    ogrenciler.update({ad: yas})

print(ogrenciler)



#dict içinde dict
ogrenciler = {}

for i in range(2):
    no = input("Öğrenci numarası: ")
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    
    ogrenciler.update({
        no:
          {"ad": ad, "soyad": soyad}
    })

print(ogrenciler)


##toplu eklemek için
ogrenciler = {"101": "Ali"}
yeni_ogrenciler = {"102": "Ayşe", "103": "Mehmet"}

ogrenciler.update(yeni_ogrenciler)
print(ogrenciler)

#listeyi dic. e çevirme
ogrenciler = {}
liste = [("201", "Zeynep"), ("202", "Ahmet"), ("203", "Elif")]

ogrenciler.update(dict(liste))
print(ogrenciler)