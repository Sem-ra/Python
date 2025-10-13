#SORU 1) GİRİLEN İKİ SAYIDAN HANGİSİ BÜYÜKTÜR
sayi1=int(input("1. sayıyı giriniz: "))
sayi2=int(input("2. sayıyı giriniz: "))
if(sayi2>sayi1):
    print(f"{sayi2} daha büyüktür.")
elif(sayi1>sayi2):
    print(f"{sayi1} daha büyüktür.")

# SORU 2) KULLANICIDAN 2 VİZE (%60) VE 1 FİNAL((%40) NOTU ALIP ORTALAMA HESAPLAYIN
vize1=int(input("1. vize notunu giriniz: "))
vize2=int(input("2. vize notunu giriniz: "))
final=int(input("Final notunu giriniz: "))
Ortalama=((vize1*20)/100) +((vize2*20)/100)+((final*40)/100)
print(Ortalama)

#SORU 2)EĞER ORTALAMA ELLİNİN ÜZERİNDE İSE GEÇTİ DEYİN
if(Ortalama>50):
    print("Geçti.")

#SORU 3)GİRİLEN BİR SAYININ TEK Mİ ÇİFT Mİ OLDUĞUNU EKRANA YAZDIRIN 
sayi=int(input("Sayi giriniz: "))
if(sayi%2==0):
    print("Sayi çifttir.")
elif(sayi%2==1):
    print("Sayi Tektir.")
   
#SORU 4) GİRİLEN BİR SAYININ NEGATİF Mİ POZİTİF Mİ OLDUĞUNU EKRANA YAZDIRIN 
sayi3=int(input("Sayi giriniz: "))
if(sayi3<0):
    print(f"{sayi3} Negatiftir.")
elif(sayi3>0):
    print(f"{sayi3} Pozitiftir.")
elif(sayi==0):
    print(f"{sayi3} nötrdür.")

#SORU 5) PARoLA VE EMAİL BİLGİSİNİ İSTEYİP DOĞRULUĞUNU KOTROL EDİNİZ
email=input("Kullanıcı adınızı giriniz: ")
sifre=int(input("şifre giriniz: "))
if(email=="sadikturan" and sifre==12345):  
    print("Giriş Başarılı")
elif(email!="sadikturan" or sifre!=12345):
    print("Giriş Başarısız")