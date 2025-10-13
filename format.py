website= "http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Proglama"
#'course' karakter dizinde kaç karakter bulunur

print(len(course))

#website içinden www karakterlerini alın
print(website[7:10])
print(website[22:25]) # website içinden com al


# course içinden ilk 15 ve son 15 karakteri alın3
print(f"{course[0:15]} {course[-15:]} ")  # son 15 hane için diğer yol course[25:41]

#course ifadesindeki karakterleri tersten yazın
print(f"{course[:-42:-1]}")

#(nereden başlayacağım, ne kadar gideceğim)

#name, surname,age,jop Bora bıdı 39 mühendis
name="bora"
surname="bıdı"
age=39
jop="Mühendis"

print("Benim Adim {} soyadim {} yasim ise {} ve meslegim {}".format(name,surname,age,jop)) # yazı yazma kısmı {} {}" ".format(değişkenadlar,değişkenadları)
print(f"Benim adım {name} soyadım {surname} yaşım {age} ve mesleğim {jop}")

a="Hello world"
print(f"{a[0:6]}W{a[7:12]}")

b=a.replace("w","W")
print(b)

# abc 3 defa yan yana yazdırın
# s="abc"

# print(f"{s} {s} {s}")
i=10
for z in range(i):

    print(i)
    z="abc"
    
      #range mesafe demek range(kaçtekrar)
    print(z,end=" ")  # end""  end yanyana yazdırmak için ve " "boşluk bırakmak için

#     # print(("abc "*3).strip())

#     #message = " Merhaba ben tuncay "

# #message = message.upper() #tüm harfler büyük
# print(message)
# message = message.lower() #tüm harfler küçük
# print(message)
# message = message.title() #tüm kelimelerin ilk harfi büyük
# print(message)
# message = message.capitalize() #mesajın sadece ilk kelimesinin ilk harfi büyük
# print(message)
# message = message.strip() #baştaki ve sondaki boşlukları siler
# print(message)
# message = message.split() #kelimeleri boşluklara göre birbirinden ayırır.
# print(message)
# message = "--".join (message) #ayrılan kelimeleri birleştirir " " içine koyduklarımız birleşmede aralarına koyulacak şeyleri ifade eder.
# print(message)
# index = message.find("tuncay") # " " içindeki kelimeyi arar bulursa kelimenin ilk harfinin indexini verir, bulamazsa -1 sonucu verir.
# print(index)
# isFound = message.startswith("M") #message'nin M ile başladığını mı sorar dönüşü True yada False olarak verir.
# print(isFound)
# isFound = message.endswith("y") # messagenin sonu y ile mi bitiyor, true false döndürür.
# print(isFound)
# message = message.replace("tuncay", "halil") # tuncay yazan yere halil yazar.
# print(message)
# message =  
# message.center
# (50, "*") # 1.parametre 50 boşluğa mesajı ortalar, 2.parametre bu boşlukları yıldızla doldurur. boşlukta olabilir.
print()
  
message=" Hello World "
d=message.strip()
print(d)

message="www.sadikturan.com"
e=message.split(".")
print(e[1])
 
course="Python Kursu: Baştan Sona Python Proglama"
f=course.lower()
print(f)

website= "http://www.sadikturan.com"
result=website.count('a')
print(result)

#website www başlayıp com ile bitiyor mu

a=website.startswith("www")
print(a)


b=website.endswith("com")
print(b)

#websitenin içinde .com var mı
g=website.find(".com")
print(g)

#course içindeki kelimeler alfabetik mi (isalpha--> alfabetik mi  ||  isdigit--->rakam mı)
h=course.isalpha()
print(h)

i=course.isdigit()
print(i)

#contents kelimesini 50 karakter içine yerleştirip sağ ve soluna * koyun
j="contents"
j=j.center(50,"*")
print(j)

# course taki bütün boşluk karakterlerini - ile değiştirin
k=course.replace(" ","-")
print(k)

#hello world deki hello ifadesini there ile değiştirin
l="hello world"
l=l.replace("world","there")
print(l)

#course boşluklardan ayırın
m=course.split(" ")
print(m)