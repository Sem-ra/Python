#SORU 1) GİRİLEN BİR SAYININ  0-100 ARASINDA OLUP OLMADIĞINI KONTROL EDİNİZ

sayi=int(input("Sayi giriniz: "))
result=(sayi>0)or(sayi<100)
print(f"SAYININ  0-100 ARASINDA OLMA DURUMU: {result} ")

#SORU 2 GİRİLEN BİR SAYININ pozitif çift  OLUP OLMADIĞINI KONTROL EDİNİZ
sayi=int(input("Sayi giriniz: "))
result=(sayi%2==0) and (sayi>0)
print(f"SAYININ POZİTİF ÇİFT OLMA DURUMU: {result} ")

#SORU 3) eMAİL VE PARALO BİLGİLERİ İLE GİRİŞ KONTOROLU YAPINIZ
email="Semra"
parola=1245
mailGiris=(input("Emailinizi giriniz: "))
ParolaGiris=int(input("Parolanızı giriniz: "))
IsGiris=(mailGiris==email) and (ParolaGiris==parola)
print(f"Girişin başarılı olma durumu: {IsGiris}")

#SORU 4) GİRİLEN 3 SAYIYI BÜYÜKLÜK OLARAK KARŞILAŞTIRINIZ.
sayi1=int(input("1. Sayıyı giriniz: "))
sayi2=int(input("2. Sayıyı giriniz: "))
sayi3=int(input("3. Sayıyı giriniz: "))
a=sayi1>sayi2 and sayi1>sayi3 and sayi2>sayi3  #123
b=sayi2>sayi1 and sayi2>sayi3 and sayi1>sayi3  #213
c=sayi3>sayi2 and sayi3>sayi2 and sayi1>sayi2  #312
d=sayi3>sayi2 and sayi3>sayi1 and sayi2>sayi1  #321
e=sayi2>sayi3 and sayi2>sayi1 and sayi3>sayi1  #231
f=sayi1>sayi2 and sayi1>sayi3 and sayi3>sayi2  #132
print(a,b,c,d,e,f)

#SORU 5) KULLANICIDAN 2 VİZE (%60) VE FİNAL(%40) NOTUNU ALIP ORTALAMA HESAPLAYIN. EĞER ORTALAMA 50 DEN BÜYÜKSE GEÇTİ. DEĞİLSE KALDI YAZDIRIN
#ortalama 50 olsa bile final notu en az 50 olmalıdır. Finalden 70 alındığında ortalamanın önemi olmasın 
vize1=int(input("1. vize notunu giriniz: "))
vize2=int(input("2. vize notunu giriniz: "))
final=int(input("Final notunu giriniz: "))
Ortalama=((vize1*30)/100) +((vize2*310)/100)+((final*40)/100)
if((Ortalama>50 and final>=50) or (final>70)):
    print("geçti")
else:
    print("kaldı")

# SORU 5 KİŞİNİN AD KİLO VE BOY BİLGİLERİNİ ALIP KİLO ENDKSLERİNİ HESAPLAYINIZ
# 0-18,4 zayıf
# 18,5-24,9 normal
# 25-29 fazla kilolu
# 30-34 obez
ad=(input("isim giriniz: "))
boy=float(input("boy  giriniz: "))
kilo=int(input("kilo giriniz: "))
kiloEndeks=kilo/boy**2
if(kiloEndeks>0 and kiloEndeks<=18.4):
    print("zayıf" )
elif(kiloEndeks<=24.9):
    print("normal" )
elif(kiloEndeks<=29):
    print("fazla" )
else:
    print("obez")

