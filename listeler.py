#"Bmw", "Mercedes", "Opel", "Mazda" elemanlarına sahip bir liste oluşturunuz
List=["Bmw", "Mercedes", "Opel", "Mazda"]
print(List)

#liste kaç elemanlıdır.
print(len(List))

#Listenin ilk ve son elemanı  // son eleman -1. indeks
print(List[0],List[3])

# #Mazda değerini toyota ile değiştir // ya da List[-1]="Toyoto" da diyebilirdik
List[3]="Toyoto"
print(List)

#Mercedes listein bir elemanı mıdır // aranacakolan in Değişken adı içerisinde var mı kontrol eder
print("Mercedes" in List)

#Listenin -2 indeksindeki eleman nedir
print(List[-2:-1])

#Listenin ilk 3 elemanını alın // [0:3] [:3] [-2:] aynı şey
print(List[:3])

#Listenin son iki elemanı yerine Renault ve Toyoto elamnlarını ekleyin
# Lidt[-2]=["Toyoto","Renault"] son iki eleman değişti

List[2]="Renault"
List[3]="Toyoto"

#audi ve nissan emanlarını listeye ekle
# result = List + ["Audi","Nissan"] list listesine yeni bir liste ekledik. yeni liste result oldu
List.append("Audi")
List.append("Nissan")

print(List)
#Listenin son elemanını silin
# del List[-1] son elemanı sildi
List.remove(List[-1]) # -1 son eleman
print(List)

#Liste elemanlarını tersten yazdırın // düzden gitsin desetdi [::1] derdik
print(List[::-1])

#Aşağıdaki veriler bir liste halinde saklayınız
# studentA= Yiğit Bilgi,2010,(70,60,70)
# studentB= "Sena Bilgi,2012,(70,80,90)"
# studentC= Yiğit Turan,1990,(78,65,70)

StudentA=["Yiğit Bilgi","2010",[70,60,70]]
studentB=["Sena Bilgi","2012",[70,80,90]]
studentC=[ "Yiğit Turan","1990",[78,65,70]]
print(StudentA)
Ogrenci_List=[StudentA,studentB,studentC]
print(Ogrenci_List[1])
print(StudentA[2][2])


# value = min(numbers) # en küçük sayıyı alır
# value = max(numbers) # en büyük sayıyı alır
# value = min(letters) # alfabetik olarak aramaya baştan başlar 
# value = max(letters) # alfabetik olarak aramaya sondan başlar

# numbers.append(49) #listenin sonuna eleman ekleme
# numbers.insert(3, 78) # 3'ü indeksten önce 78 sayısını ekle. 
# numbers.pop(0) # indeks numarası 0 olan elemanı siler
# numbers.remove(49) # 49'u siler 
# numbers.sort() # küçükten büyüğe sıralar
# numbers.reverse() # büyükten küçüğe sıralar
# letters.sort() # alfabetik olarak sıralar
# letters.reverse() # o anki halini indexe göre olarak TERSTEN sıralar

# print(numbers.count(10)) # numbers listesinin içinde kaç tane 10 var
# print(letters.count("a")) #letters listesinin içinde kaç tane a harfi var.
# numbers.clear #temizler. 

# result = names.remove('Deniz')
# print(result)
# satırı, ekrana None yazdırır. Çünkü remove() işlemi başarılı olsa da, result değişkenine atanan değer None'dur.

names= ['Ali','Yağmur','Hakan','Deniz']
years= [1998,2000,1998,1987]

#Cenk ismini Listenin sonuna ekleyiniz
names.append("Cenk")
print(names)

#"Sena" değerini listenin başına ekleyiniz
names.insert(0,"Sena")
print(names)   

# #Deniz ismini listeden siliniz
#names.remove('Deniz')   #names.pop() listedeki son elemanı siler
                          #names.pop(index)
# print(names)

#Deniz isminin indeksi nedir
names.index("Deniz")
print(names)

#Ali listenin bir elemanı mıdır
result='Ali' in names
result=names.index("Ali")



#liste elamanlarını ters çevirin
names.sort()
print(names)
names= ['Ali','Yağmur','Hakan','Deniz']
names.reverse()
print(names)
# eğer sort la alfabetik sıraya sokmazsak o anki halini tersten yazıyor.
# sort yapıp reverse yaparsak ters alfabetik sıralıyor z-a tya

#Liste elemanlarını alfabetik sıralayın
names.sort()  
print(names)

#years listesini rakamsal büyüklüğe göre sıralayın
years.sort()
years.reverse
print(years)

# str="Chevrolet, Dacia" karakter dizisini listeye çevirin
# str="Chevrolet,Dacia" 
# a=str.split("")
# print(a)
str1 = "Chevrolet,Dacia"
liste = list(str1)  #List metodu ile ayırdık
print(liste) 




#years Dizinin en büyük ve en küçük elemanı
result=min(years)
print(result)
result=max(years)
print(result)

# years dizisin kaç tane 1998 var
print(years.count(1998))

# years dzisinin tüm elemanlarını siliniz
years.clear()
print(years)

# kullanıcıdan alacağınız 3 tane marka bilgisini listeye ekle
# markalar=[]
# for i in range(3):
#     a=input(f"{i+1}. markayı girin: ")
#     markalar.append(a)
#     print(markalar)
