

# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. Dosyayı konumda oluşturur.
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.


#open("newfile.txt","r") #ile açarsak aynı dosya içinde olmalı o yüzden ilk aşamada w modunda açılmalı
result=open("newfile.txt","w") 
file=open("newfile.txt","w")
file.close() #a.ılan dosya kapatılmalı


# w modu her seferinde çalıştırıldığında bir önceki verileri siler

file = open("newfile.txt","w")
file = open("C:/users/sadikturan/desktop/newfile.txt","w")
file.close()
#dosya farklı kasörde ise

file=open("newfile.txt","w",encoding='utf-8')
file.write("Sadık Turan")
file.close()
#w da içerik silinir
print(result)

#a modu
#içerik silinmez ekleme yapar
file=open("newfile.txt","a",encoding='utf-8')
file.write("\nSadık Turan") # new line \n 
file.close()

#x modu dosya oluşturmak için kullanılır
ile=open("newfile2.txt","x",encoding='utf-8') # tekrar oluşturursak hata verir dosya zaten oluşturulduuna dair
file.write("Sadık Turan")
file.close()

#dosyayı kapatma sebebimiz açık kalıp kaynakları tüketmemesi


# türkçe karalter tanıma encoding='utf-8'
# dosyanın modu belirtilmezse varsayılan mod r dir


file=open("newfile.txt1","r",encoding="utf-8")
#r modunda dosya oluşmuş olmalı yoksa bize hata verir

#1. yntem
for i in file:
    print(i,end="")

# read fonsk.
content=file.read()
print(content)









