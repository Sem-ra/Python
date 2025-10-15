# #Göderilen bir kelimeyi belirtilen kez ekranda gösteren foks. yazın

# def kelimeYazdir():
#     kelime=input("Kelime yazın: ")
#     defa=int(input("Kaç defa kelime yazsın:" ))
#     i=0
#     while i<defa:
#         print(kelime)
#         i+=1

# kelimeYazdir()

# #Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonks. yazın

# def listeyeCevir(*params):  ## * tek yıldızda tuple tipi liste ** çift yıldızda dictionary belirttiğimiz anlamına gelir
#     liste1=[]
#     liste1.append(params)
#     print(liste1)

# listeyeCevir(1,2,3)

# #Gönderilen 2 sayı arasındaki tüm asal sayıları bulun

# def AsalBul():
#     baslangic=int(input("Başlangıç değerini giriniz::" ))
#     bitis=int(input("Bitis değerini giriniz::" ))
#     sayi=baslangic
                    
#     for i in range(baslangic,bitis):
#         if(i<2):
#             i+2


#         for a in range(2,i):
#             if(sayi%i!=0):
#                 i-=1
#             else:
#                 break
#         print(sayi)
#         i+=1


#         AsalBul()
#     # Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonks yazın

   

#     # def SayininTamBölenleri():
#     #     sayi=int(input("Sayiyi giriniz::" ))
#     #     for i in range(sayi):
#     #         for i in range(sayi):
#     #             if(sayi%i==0):
#     #                 print(f"{sayi} nın tam bölenleri: ",end=" ")
#     #                 print(i)
#     #                 i-=1

#     def SayininTamBölenleri():
#         sayi=int(input("Sayiyi giriniz::" ))
#         for i in range(1,sayi+1):
            
#             if(sayi%i==0):
#                 print(f"{sayi} nın tam bölenleri: ",end=" ")
#                 print(i)
                  

#     SayininTamBölenleri()

# ##Sınıf üzerinde tanımlanan fonksiyonlara method denir. sınıf üzerinden çağrılıyorsa methoddur. Sınıfsız kullanılıyorsa fonksiyondur.
# ##Fonksiyonlar belirli bir işi yapmak için kullanılır.
# ##Fonksiyon tanımlarken def anahtar kelimesi kullanılır.
# #Tuple ve dictionary türünde parametre gönderme:
# #Tupple şeklinde gönderilecekse *params kullanılır.
# ##Örnek:
# #     def toplam(*params):
# #         return sum((params))
    
# #     print(toplam(10,20,50))

# #     Eğer dictionary tarzında olacaksa **params kullanılır.
# # #Örnek: def fonk(**params):  # ya da def fonk(**args):  
# # # print(fonk(isim="Ali",soyisim="Yılmaz"))
# # # çıktı: {'isim': 'Ali', 'soyisim': 'Yılmaz'}


# # myfunc(a,b,*args,**kwargs):  # args tuple, kwargs dictionary türündedir.
# # print(a)
# # print(b)
# # print(args)  # args tuple türündedir.
# # print(kwargs)  # kwargs dictionary türündedir.
# # myfunc(10,20,30,40,50,isim="Ali",soyisim="Yılmaz")
# # a ve b ile 1. ve 2. parametre eşleşiyor. key value tipine kadar olanı da arg alıyor.
# # a ve b ile 1. ve 2. parametre eşleşiyor. key value tipine kadar olanı da *arg olan parametre alıyor.

# def toplam(*params):
#     return sum((params))

# print(toplam(10,20,30,40,50,200,300))

# print(sum((1,2,3,4,5,6,7)))  # tuple türünde parametre gönderme

for i in range(5,11):
    if(i<1):
        break
    for j in range(2,i):  
        if(i%j==0):
            print(f"{i} asal değildir.")
            break
        else:
            print(f"{i} asaldır.")

# range(başlangıçdeğeri, bitişdeğeri, artışmiktarı)
# range(0,10,+1)
# range(10,-1,-1) 10 9 8 7 6 5 4 3 2 1 0