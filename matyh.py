# import math
# import math as islem

# value = dir(math)  #value yı print ile yazıdırınca math içindeki tüm fonks. bilgilerini verir
# value = help(math) # value print edince fonks. açıklamasını getirir
# value=math.ceil(5.9)
# value= islem.factorial(5)


# from math import* # yıldız ile hepsi diye belirtmiş olduk
# #tüm math fonks. getir demiş olduk. o yüzden ismini söylemeye gerek olmadan direkt fonks. kullanabiliyoruz


# from math import factorial,sqrt,ceil
# #burada istediklerimizi import etmiş olduk
# value=factorial(5)
# value=sqrt(5)


# def sqrt(x):
#     print('x:' +str(x))

#     #en son hangisi tanımlandıysa onu seçer o yüzden burada def i kullanır.
#     #math kütüphanesi bizim tanımladığımız kütüphaneden sonra tanımlansaydı o zaman math kütüphanesini kullanırdı.

#---------------
import random
# result = dir(random) #fonks.
# result=help(random) # fonsk içerikleri


result=random.random()  #o.00 ile 1.00 arasındaki sayıları üretir
result=random.random() * 100 #üretilen sayılar 100 ile çarpılır

greeting="hello there"
result = random.uniform(1,10)
result=int(random.uniform(10,100)) #tam sayıları getirir
result=random.randint(1,100) #tam sayıları alır

names=['ali','yağmur','deniz','cenk']
result=names[random.randint(0,len(names)-1)]
result=random.choice(names) #choice metodu rastgele seçer
result=random.choice(greeting)

liste=list(range(10))
random.shuffle(liste) # liste karışık sırada gelir
result=liste
result=random.sample(liste,3) #listeden rastgele 3 tane sayı getir
result=random.sample(names,3) #rastgele 2  isim getir listeden



print(result) 



