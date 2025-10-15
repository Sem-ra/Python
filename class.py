#class

## class keyword ü kullanılarak class oluşturulur
## class isimleri büyük harfle başlamalıdır.
## class ların içerisinde fonksiyonlar ve değişkenler tanımlanabilir.
## class ların içerisinde tanımlanan fonksiyonlara method denir.
## class ların içerisinde tanımlanan değişkenlere attribute denir.
## class ların içerisinde tanımlanan method ve attribute lara erişmek için self keyword ü
## kullanılır.
## self keyword ü class ın kendisini temsil eder.
## class ların içerisinde tanımlanan method ların ilk parametresi self olmalıdır.

# class Person:
#     #class attribute
#     address="No information"
#     #constructor method
#     def __init__(self,name,year):
#         #object attribute
#         self.name=name
#         self.year=year
#         print("init methodu çalıştı.")
    
#     #instance method
#     def intro(self):
#         print(f"Hello my name is {self.name} and I'm {self.getAge()} years old.")
    
#     def getAge(self):
#         return 2024 - self.year

# class Person:
#     pass #"pass" ifadesi class ın boş olduğunu belirtir.
#    #attribute ve method tanımlanmadığında kullanılır.
#    #method ve attribute tanımlandığında pass ifadesine gerek yoktur.

# #    object(instance)

# p1=Person() #person1 nesnesi person class ının bir örneğidir.
# p2=Person() #person2 nesnesi person class ının bir örneğidir.
# print(type(p1)) #<class '__main__.Person'>
# print(type(p2)) #<class '__main__.Person'>
# print(p1) #<__main__.Person object at 0x000001E4C8B3D9A0>
# print(p2) #<__main__.Person object at 0x000001E4C8B3D9D0>


# Attribute hem class hem de object üzerinde tanımlanabilir.
# object cunstructor ı ile object oluşturulur.
from os import name
from typing import Self


class Person:
    # pass
    #class attribute
    address="No information" #bunu tanımladıktan sonra pass i kaldırabiliriz.
    #constructor method (oluştıulan object i başlatmak için kullanılır)
    def __init__(self, name, year):  # self objectleri kastediyor
        self.name = name
        self.year = year
        print("init methodu çalıştı.")
    def intro(self): #self yazmasak hata verir. objeye hizmet eder etmeli
        print(f"Hello Tehere. My name is {self.name}.")
    def getAge(self):
        return 2025 - self.year
    
p1 = Person("ali", 1990)
p2 = Person("veli", 1985)
print(f"p1 name: {p1.name} year: {p1.year}")
print(f"p2 name: {p2.name} year: {p2.year}")
p1.intro()
p2.intro()
print(f"adım: {p1.intro} p1 age: {p1.getAge()}")
print(f"adım: {p2.intro} p2 age: {p2.getAge()}")

# updating
p1.name = "ahmet"
p1.year = 2000
print(f"p1 name: {p1.name} year: {p1.year}")


# şablon
# class adı
#    pass(eğer özellik ve method tanımlanmadıysa)
#     Attribute (özellikler)
#     methodlar

# atributes lar hem class hem de object üzerinde tanımlanabilir.
# # object cunstructor ı ile object oluşturulur.
# # class ın içindeki method ların ilk parametresi self olmalıdır.
# # self class ın kendisini temsil eder.
# # class ın içindeki method ların ilk parametresi self olmalıdır.
# cunstructor
# def_init_(self, parametreler)
# yapıcı olmasının sebenebi __init__ methodunun class ın bir parçası olmasıdır. ve her bir nesne için çalışmasıdır
# self yerine this de kullanılabilir ama self daha yaygın kullanılır.


class Circle:
#class obejct attribute
    pi=3.14
    #constructor
    def __init__(self, yaricap=1):
        self.yaricap=yaricap
    #methods    
    def cevre(self):
        return 2*self.pi*self.yaricap
    def alan(self):
        return self.pi*(self.yaricap**2)

c1=Circle() #yarçapı belirtmezsek default olarak 1 alır
c2=Circle(5)
print(f"c1 yarıçap: {c1.yaricap} alan: {c1.alan()} çevre: {c1.cevre()}")
print(f"c2 yarıçap: {c2.yaricap} alan: {c2.alan()} çevre: {c2.cevre()}")
