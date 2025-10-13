#value types => string, number(int, float)
#---------------------------------------

# x = 5
# y = 25

# x = y

# y = 10

# print(x,y)   # y'nin üzerinde yaptığım değişiklik x'i etkilemedi. çünkü value tipli

#reference types => list
#---------------------------------------
# a = ["apple", "banana"]
# b = ["apple", "banana"]

# a = b 

# b[0] = "grape"

# print(a, b) #b'de yapılmış bir değişiklik a'yı değiştirdi. çünkü referans tipli.

#referans tipli değişkenleri adres bilgisi olarak düşünebilirsiniz. o adresi gösterirler.
#a ile b yi eşitlediğimiz zaman aynı adresi gösteren değişkenler oluyorlar
#bu yüzden a üzerinde yapılan değişiklikler adresde olan değişiklikler olduğu için b'de değişiyor.

#value tipli değişkenler değer taşırlar o yüzden her hangi bir adresi refarans olarak göstermezler.
#x ile y i eşitlediğimde değerleri değişir. 
#sonrasında herhangi birini değiştirirsek diğerini etkilemez. 







#Soru: 
x,y,z=2,5,107
numbers=1,5,7,10,6

#Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamınun farkı nedir

#input hep string alır eğer int bir değer alacaksak int dönüşümü yapılacak
sayi1=int(input(f"1. sayıyı girin: "))
sayi2=int(input(f"1. sayıyı girin: "))
a= (sayi1)*(sayi2) 
b=x+y+z
print(f"Fark: {a-b}")

#y'nin x e kalansız bölümmünü hesaplayınız
kalansiz=y//x
print(f"Kalansız bölme: {kalansiz}")
## Kalansız bölme yani int alması için Bölme de // kullanılır.

#(x,y,z) toplamının mod 3 nedir
toplam=(x+y+z)
print(f"Mod3: {toplam%3}")

#y nin x kuvvetini hesaplayın
us=y**x
print(f"Y**x = {us}")

# x, *y,z = numbers işlemine göre z nin küpü kaçtır.
# *y --> listedeki elemanlar değişkenlere atanırken fazla kalan elemanları kendi içine çekiyor
x,*y,z=numbers #numbers=1,5,7,10,6
print(x,y,z)  # 1,5,7,10,6 x=1 y=5,7,10 z=6 olur
print(f"Z'nin küpü: {z*z*z}")
print(y)
# t,k,l=y
# print(f"Y nin elemanları toplamı: {t+k+l}")
# toplam=0
for i in range(len(y)): # y listesinin eleman sayısı kadar çalış
    toplam+=y[i]

print(toplam)

