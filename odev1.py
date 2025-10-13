metin="Eros magna feugait sea minim diam consequat zzril nulla nonumy esse mazim erat velit sit sanctus justo accusam sea elit amet sed vero blandit nostrud magna dolore nisl lorem dolor magna kasd at dolore no accusam facilisis sit sit tincidunt amet in vero ipsum dolore erat diam sed et elit duo ut aliquip vero tempor vel laoreet sed ut magna no rebum sit dolore eros sanctus aliquyam sit sed at"
print(metin)
#1)Metin kaç kelimeden oluşuyor.
print(len(metin))
metin=metin.split() #boşluklardan metni ayırdık. split() ile boşluklardan (veya başka bir ayırıcıdan) ayırdığında sonuç zaten bir liste olur.
print(type(metin))  # liste
print(len(metin)) #70 tane
# # metinList=list(metin) #Burada metni listeye çevirdik. Bu da list ile listeye çevrilmiş versiyon.
# # print(type(metinList))  # liste
# # print(metinList)
    # split ile ayırarak zaten liste oluşturduk. Onu kullandık. iki yöntem de burada kalsın.
    # Liste oluşturmak için ---> metinList=list(metin)  ya da metin=metin.split()
print(metin)
# 2) 22. kelime nedir? 
print(metin[21]) #index sıfırdan başlıyor. 21. index 22. elaman oluyor

#3)Tekrarlanan kelimeler tekrarlanmadığında kaç kelime kaldığını hesaplayan kodu yazınız?
#Tekrarlanan kelimeleri listeden çıkaran ---> sets ile tekrarlanan elemanlar çıkarılır
tekrarsizMetin=set(metin)
print(tekrarsizMetin)
print(len(tekrarsizMetin)) #45 tane

# 4) Dizi haline gelen metnin elemanlarını alfabetik tersten sıralayan kod nedir?
# numbers.sort() # küçükten büyüğe sıralar
# numbers.reverse() # büyükten küçüğe sıralar
# letters.sort() # alfabetik olarak sıralar
# letters.reverse() # o anki halini indexe göre olarak TERSTEN sıralar
# a=metin.reverse() print(a) --> Bu olmaz. Çünkü Python’da .reverse() listenin kendisini ters çevirir ama geriye None döner.reverse() → listeyi yerinde değiştirir, ama sonuç döndürmez.Bu yüzden a değişkeni None olur.
# O yüzden metin.reverse()  yapıp print(metin) yazıdırılmalı. ama bizden istenen öncelikle sıralamak.

metin.sort()
metin.reverse() # burada zaten tersine çevirdi.yazdır dediğimizde ters çevrilmiş versiyonu yazacak.
print(metin)  #Büyük küçük harf sıralamayı etkiliyor. Python’da sort() varsayılan olarak ASCII/Unicode değerlerine göre sıralar. Bu yüzden büyük harfler küçük harflerden önce gelir.

ogrenciler=["tuncay","nazli","berat","semra"]
# 5)Yukarıdaki listeye 3 öğrenci ekleyeceğiz. öğrencileri kullanıcıdan alacağız ve kullanıcı öğrenci ismini eklerken
# "eklenecek 1.öğrencinin ismini girin: ”
# “eklenecek 2.öğrencinin ismini girin: ”
# “eklenecek 3.öğrencinin ismini girin: ”
# mesajlarını görecek. Tabiki bizde bu mesajları tek tek elle yazmayacağız. Uygun kodu yazın.
 #cevap:
for i in range(1,len(ogrenciler)):
    ogrenci=input(f"{i}. öğrenciyi girin:")
    ogrenciler.append(ogrenci)
print(ogrenciler)
 # add tek tek ekliyor. insert ile eklemek için --> insert(index, x) →  (x ile elaman kastediliyor. o yüzden o da tek ekliyor )istediğin sıraya ekler. o yüzden burada uygun değil.

#6) Kullanıcıdan değiştirmek istediği öğrencinin index numarasını verdiği bir input alacağız ve girilen index numarasındaki öğrencinin adını değiştirmesi için bir input daha alacağız. Buna uygun kodu yazın
#cevap:
no=int(input("Lütfen değiştirmek istediğiniz öğrencinin index numarasını giriniz: "))
ogrenciler[no]=input("Lütfen öğrencinin yeni ismini giriniz: ")
print(ogrenciler[no])
print(ogrenciler)

#7) Kullanıcıdan alacağımız ismi, listeden silecek kodu yazın
no=int(input("Silmek istediğiniz öğrencinin index numarasını giriniz: "))
ogrenciler.pop(no) # nedense remove ile olmadı.Öğrenciler listede string tutuluyor. Eğer kullanıcıdan aldığımız girdiyi string yaparsak olur.remove da olur
print(ogrenciler)

isim=input("Silmek istediğiniz öğrencinin ismini giriniz: ")
ogrenciler.remove(isim)  #input u string alınca remove çalıştı.
print(ogrenciler)

#pop(index) → index’e göre siler.

#remove(value) → elemanın değerine göre siler. yani elemanı yazmak gerekiyor.Ama biz kullanıdan aldığımız ismi index üzerinden atayıp listeye ekledik

# #8) Kullanıcıdan alacağımız 3 tane şehir ve plaka isimlerini yukarıdaki dictionary’e ekleyecek kodu yazın.
sehirlerPlakalar = { "ankara" : 6, "istanbul": 34, "bursa": 16, "antalya": 7}
for i in range(0,3):
    plaka=input("plaka giriniz: ")
    sehir=input("şehrin adını giriniz: ")
    sehirlerPlakalar.update({sehir:plaka})


print(sehirlerPlakalar)



#9) Kullanıcını şehir ismi girince o şehrin plakasını yazdıracak kodu yazın.
sehir=(input("Şehir adını giriniz: "))

print(sehirlerPlakalar[sehir])


'''
10) Yukarıda referans tipli veri türlerinde sırayla atamalar gerçekleşmiştir. 1.Fotoğrafta
listeleri değişkenlere atadıktan sonra, diğer fotoğraflardaki işlemleri birbirlerine
eşitleyerek, yukarıda olanları kodlayınız.
'''
#Toplu yorum satırı için """....."""  ya da '''.....''' kullanılıyor. Normalde bunları string algılıyormuş ama atama yapılmadığı için slorun olmuyormuş

#cevap:
a={"elma","armut"} #1
c={"kivi","portakal"} #2
b={"mandalina","ananas"} #3

print(a,b,c)
# a  1. adreste(e,a)   3  2
# b  3. adreste(ma)    2  2
# c  2. adreste(kp)    1  2

temp=a #1 
a=b #3
b=c #2
c=temp #1

print(a,b,c)


a=b
c=b
print(a,b,c)














