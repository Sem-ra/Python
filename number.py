# print("merhaba")
# print(2+2)
# maasAli,maasDeli,vergi=(1000,2000,0.27)
# print(maasAli-(maasAli*vergi))
# print(maasDeli-(maasDeli*vergi))
# değişkenler yanyana virgül ile yazılabiliyor. tek satırda 
# print(10//3) # // bölümde tam kısmı alır. aşağı yuvarlar hem pozitif hem de negatif değerler için
# print(-10//3) # yine aşağı yuvarlayıp tam kısmı aldı
# print(10/3)
#değişken tanımlama^
# #
# Musteri_Ad="Nur"
# Musteri_Soyad=" Nuray"
# Musteri_AdSoyad=Musteri_Ad+Musteri_Soyad
# Musteri_Cinsiyet="K"
# Musteri_TC=102030405060
# Musteri_DogumYili=1796
# Musteri_Adres="Fransa"
# Musteri_Yas=2025-Musteri_DogumYili
# print(Musteri_Ad + Musteri_Soyad +" " + Musteri_Cinsiyet)
# print(Musteri_Ad)

# #aşağıdaki hessiparişlerin toplam bilgisini hesaplayınız.
# siparis1,siparis2,sipari3=(110,1100.5,356395)
# print(siparis1+siparis2+sipari3)


# x=input("1. sayi girin:")  #inputlar string değer alır
# y=input("2 .sayi girin:")

# """
# x=int(input("1. sayi girin:"))  #inputları string almaktan int  değer almaya çevirdik. Artık kullanıcı int giriş yapmalı
# y=int(input("2 .sayi girin:"))
# """

# toplam=x+y
# print(toplam)
# # Toplam = int(x) + int(y)
# # print(Toplam)
# # print(type(Toplam))

# """
# type Conversion (Tür Dönüşümleri)

# int to float
# float to int
# str to int
# bool to str  
# bool to int   aldığı değer true=1  false=0

# type() ---> tür bilgisi alıyoruz
# """



# YariCap=float(input("yarı çapı girin: "))
# pi=3.14
# Alan=(YariCap**2)*pi
# print(Alan)
# DaireCevre=2*YariCap*pi
# print(DaireCevre)
# print(type(DaireCevre))
# print(type(YariCap))


Ad="semra"
Soyad="Cebeci"
Yas=36
AdSoyad="Benim adım "+ Ad + " ve Soyadım "+ Soyad + " yaşım ise " + str(Yas) 
print(AdSoyad)

print(Ad[0])
a=len(Ad)
print(a)
print(len(AdSoyad))
print(Ad[0:4]) 
print(Soyad[0:4:2])
print("Ad\nSoyad")  # \n alt satıra geçmek için fakat sadece str de kullanıldığından dolayı " " ları unutma

#alt+z sağ tarafa kaymayı önlüyor
#stringler dizidir.
print(Ad[-5])
print(Yas)

name="İsim"
surname="Soyisim"
age=17
print(f"{name} bilgisi ile {surname} bilgisi ve {age} içerir")
result=200/700
print('{r:9.5}'.format(r=result)) # r : bu kısım ne kadar boşluk verileceği . sonraki ise kaç haneyi yazdıracağı




