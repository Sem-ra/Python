"""
Sinif, nesne (object) üretmek için kullanilan bir şablondur (template)
Sinif içinde özellikler (attributes) ve davranişlar (methods) tanimlanir.

__init__ : kurucu metot: siniftan her yeni nesne(örnek) oluşturulduğunda otomatik çalişir.

self: Sinifin kendisini temsil eden özel bir kelimedir. Yani self.name demek, bu nesneye ait name alani demektir.

self.name → sinifa (nesneye) ait özellik (attribute),yani bu değer artik o nesnenin içinde saklanir.
self.name, Nesnenin içindeki kalici özellik, Nesne var oldukça kullanilabilir.

name ->Dişaridan gelen geçici parametre, Fonksiyon çağrilirken kullanilir

“Parametreyle gelen name değerini al,ve bunu bu nesnenin self.name adli özelliğine ata.” demektir.
 Self sadece o nesneyi (objeyi) temsil eder — yani “bu nesnenin içindeki şeyler” demek.                                       

class sinifAdi:
    def__init__(self,name,surname):         
        self.name=name                      
        self.surname=surname 


Kalitim(Inheritance)
Kalitim, alt sinifin üst sinifin özelliklerini ve metotlarini kullanabilmesidir.
Alt sinif tanimlanirken, miras alacak sinif parantez içinde belirtilir.

class Student(Person):
-----------------

üst sinifin kurucu metodu çağrilir ve üst siniften kullanilacak özellikler belirtilir.Üst sinifin Kurucu metodunu çağirmak için 2 yöntem var
Tercih edilen yöntem --> super anahtar kelimesinin kullanildiği yöntem.
1. yöntem
class Student(Person):
    def__init__(self,number,name,surname):    hem üst sinif özellikleri hem de alt sinif özellikleri parametre olarak belirtilir
    Person().__init__(self,name,surname)     Burada üst sinifitan alinacak özellikleri belirtmiş olduk
        self.number=number                    burada ise alt sinifin number parametresini self.name özelliğine aktardık


2. yöntem
class Student(Person):
    def__init__(self,number,name,surname):   
    Super().__init__(name,surname)         # fark burada selflemedik. super anahtar kelimesini kullandik.SUPER'de python zaten SELF'i biliyor.
        self.number=number


Fark ise ,
 Person().__init__(self,name,surname):  normal bir fonksiyon gibi çağrildiği için biz self'i manuel göndermek zorundayiz.
 Yani diyoruz ki person, şu self nesnesini kullarak çaliş
 super de ise self otomatik gider.

 _______________________________________________________________________________________________________
 Eğer elimizde bir person nesnesi varsa 
 p=Person("Ali","Yilmaz") 
 p.__init__("Ali","Yilmaz")   burada ise p self rolündedir.Python otomatik self=p atamasi yapar.Oyüzden self parametresi dışaridan görünmez
_______________________________________________________________________________________________
Neden super tercih ediliyor
Çünkü çoklu kalitim da karmaşayi önlüyor
Bir sinif üst siniftan çoklu miras aliyorsa buna çoklu kalitim denir.
Şimdi  Person().__init__(self,name,surname) bu kullanimda self i manuel belirtiyoruz. çoklu miras alindiğinde, birden fazka kez çağrilabilir. --> Buna diamond problem denir
Super() kulllandiğimizda python her sinifin hangi sira ile çağrilacağini otomatik hesaplar. Buna MRO(Method Resolurion Order)denir
print(SinifAdi.mro()) komutu MRO sirasini ve super in nasil sira ile çaliştiğini gösterir
Bu sebeplerle super kullanmak daha elverişli!!


OVERRİDE (METOT GEÇERSİZ KILMA) VE MİRASLA BİRLİKTE METOT KULLANİMİ
Override işlemi zaten aynı isimli metotu farkli parametrelerle kullanimi idi. O yüzden burada da alt sinifta aynı isimli metot kullanilirsa override tan bahsedebiliriz

super() ile üst metodu çağirmak hem üst sinifin metodunu korur hem de alt sinif metonu ekleme yapar.

class Person:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def bilgi_yazdir(self):
        print(f"Person: {self.name} {self.surname})

class student(Person):
    def __init__(self,number,name,surname):
        super().__init__(name,surname) 
        self.number=number
    def bilgi_yazdir(self):
        super().bilgi_yazdir()  -->burada üst sinif metodu override ediliyor
        print(f"Student: {self.number})
        
metot override alt sinif üst sinifin metodunu geçersiz kilar.yani kendi metodunu devreye sokar.Bunu da,
override var super yok--> alt sınıf metodu çalışır.üst sinif metodu çalışmaz
override var,super var --> alt sinif + üst sinit  her ikiside çalışır.


Peki bu siniflari nasil kullancağiz,
nesnesi üzerinden
s1=Student(102,"Ali","Yilmaz")
s1=Student(103,"Ali","Deli")
p1=Person("Ali","Yilmaz")

kisiler=[]
kisiler.append(s1)
kisiler.append(s2)
kisiler.append(p1)

for kisi in kisiler:
    if isinstance(kisi,Student): #student nesnesi ise
        print("Öğrenci Bilgisi:")
        kisi.bilgi_yazdir()
    elif isinstance(kisi,Person): #student nesnesi ise
        print("Person Bilgisi:")
        kisi.bilgi_yazdir()

isinstance (obj, sinif)
bu pratik fonks. bir nesnenin belirli bir sinifa ait olup olmadiğini kontrol edip bool değer döndürür true/false. eğer true ise if e girer 
Yani tek liste yapıp hangi sınıfa aitse kolayca isinstance fonks. ile işlem yapabilirim. Zaten isinstance hangi sınıfa ait kontrolünü yapıyor.







Birden fazla nesneyi yönetmek için listeler kullanilir.

#sinif isimleri büyük harfler, metot isimleri küçük harfle!







"""





#------------------------
# class Person:
#     def __init__(self,name,surname):
#         self.name=name
#         self.surname=surname

# class student(Person):
#     def __init__(self,number,name,surname): #miras alınacak özellikler parametre de belirtilir
#         Person().__init__(self,name,surname) #mirasını aldığımız sınıfın yapıcı metodunu çağırıyor.ve tekrar miras alınanlar belirtiliyor.super().__init__(name, age) böyle de olur.super de self yazılmıyor zaten içinde
#         self.number=number

# class teacher(Person):
#     def __init__(self,branch,workingTime,name,surname):
#         Person().__init__(self,name,surname)
#         self.branch=branch
#         self.workingTime=workingTime

# class employee(Person):
#     def __init__(self,workArea,workingTime,name,surname):
#         Person().__init__(self,name,surname)
#         self.workArea=workArea
#         self.workingTime=workingTime

#----------------------------------


class Person:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def getInfo(self):
        print(f"Name: {self.name}\nSurname: {self.surname}") 
        # \n ==Console.WriteLine
# class School(Person):
#     def __init__(self,name,surname,persons=None):
#         self.persons=persons or []
# #Listeyi boş tanımladık çünkü boşta olabilir eklenebilirde. 
        


class Student(Person):
    def __init__(self,number,name,surname,liste=None): #miras alınacak özellikler parametre de belirtilir
        super().__init__(name,surname) #mirasını aldığımız sınıfın yapıcı metodunu çağırıyor.ve tekrar miras alınanlar belirtiliyor.super().__init__(name, age) böyle de olur.super de self yazılmıyor zaten içinde
        self.number=number
        self.liste=liste or []
    def getInfo(self):
        print(f"Student number: {self.number}")
        super().getInfo()
    def studentList(self,kisiler):
        print("-----------------------------------------------------------")
        print("Student List:")
        print("-----------------------------------------------------------")
        print(f"{'number':<10} {'name':<10} {'surname':>10}")
        print("-----------------------------------------------------------")
        for kisi in kisiler:
            print(f"{kisi.number:<10} {kisi.name:<10} {kisi.surname:<10}")
           
    def findStudents(self,number,persons):
        for s in persons:
            if (s.number==number):
                return s
   

    

class Teacher(Person):
    def __init__(self,name,surname,branch,workingTime):  #bu sıralamayı örnekte nasil kullanacaksak ona göre belirliyoruz ("ayşe","yilmaz") mı ("yilmaz","ayşe") mi nasıl gösterim istiyorsak
        super().__init__(name,surname)
        self.branch=branch
        self.workingTime=workingTime
    def getInfo(self):
        print(f"Branch: {self.branch} \nWorking Time: {self.workingTime}")
        super().getInfo()
    def teacherList(self,kisiler):
        print("Teacher List:")
        print("---------------------------------------------------------------------------")
        print(f"{'Name':<10} {'Surname':<10} {'Barnch':<15} {'Working Time':<10}   ")
        print("---------------------------------------------------------------------------")
        for kisi in kisiler:
            print(f"{kisi.name:<10} {kisi.surname:<10} {kisi.branch:<15} {kisi.workingTime:<15}")
    def findTeacher(self,branch,persons):
        teacherr=[]
        for t in persons:
            if (t.branch.lower()==branch.lower()):
                teacherr.append(t)
        return teacherr

class Employee(Person):  
    def __init__(self,name,surname,workArea,workingTime):
        super().__init__(name,surname)
        self.workArea=workArea
        self.workingTime=workingTime
    def getInfo(self):
        print(f"Employee: {self.workArea}")
        super().getInfo()
    def employeeList(self,kisiler):
        print("Employee List:")
        print("------------------------------------------------------------------------------")
        print(f"{'Name':<10} {'Surname':<10} {'Work Area':<15} {'Working Time':<12}")
        print("------------------------------------------------------------------------------")
        for kisi in kisiler:
            print(f"{kisi.name:<10} {kisi.surname:<10} {kisi.workArea:<15} {kisi.workingTime:<18}")

            # satır arası boşluk ayarı değisken:<sayı  bilgi mesajlarında ise {bilgi:<sayı}
 
def Menu():
    print("1-Student List (S)")
    print("2-Teacher List (T)")
    print("3-Employee List (E)")
    print("4-Student Find (N)")
    print("5-Teacher Find (B)")
    
    print("6-Exit (X)")
    while(True):
        print()
        entry =input("Choose: ").capitalize()
        print()
        if (entry=="1" or entry=="S"):
            s1.studentList(students)
        elif(entry=="2" or entry=="T"):
            t1.teacherList(teachers)
        elif(entry=="3" or entry=="E"):
            e1.employeeList(employees)
        elif (entry=="4" or entry=="N"):
            number=int(input("Number: "))
            a=s1.findStudents(number,students)  
            if a:
                a.getInfo()
            else:
                print("Student not found")
        elif (entry=="5" or entry=="B"):
            branch=input("Branch: ").upper()
            print()
            t=t1.findTeacher(branch,teachers)  
            if t:
                for a in t:
                    a.getInfo()
                    print()
            else:
                print("Branch not found")                  
        elif(entry=="6" or entry=="X"):
            exit()
        else:
            print("Invalid input! Please try again.")
        
        

students=[]
teachers=[]
employees=[]
s1=Student(100,"Sezen","Aksu")
s2=Student(101,"Sezer","Aksan")
s3=Student(102,"Sezgin","Aksık")
s4=Student(103,"Sercan","Aksa")
s5=Student(104,"Sevcan","Aksun")
s6=Student(105,"Serhat","Aksup")
s7=Student(106,"Selen","Aksar")
s8=Student(107,"Seçil","Akar")
s9=Student(108,"Salih","Akın")
s10=Student(109,"Sena","Akça")
t1=Teacher("Fatma","Girik","Social Sciences",2)
t2=Teacher("Türkan","Şoray","Art",3)
t3=Teacher("Kadir","İnanır","Geometry",4)
t4=Teacher("Filiz","Akın","Mathematics",5)
t5=Teacher("Gülşen","Bubikoğlu","Music",6)
t6=Teacher("Banu","Alkan","Art",3)
t7=Teacher("Gülşen","Bubik","Music",8)
e1=Employee("Fidan","Bacı","Cleaner",1)
e2=Employee("Fazilet","Bir","Secretary",2)
e3=Employee("Ferhunde","ikinci","Menagment",5)

students.append(s1)
students.append(s2)
students.append(s3)
students.append(s4)
students.append(s5)
students.append(s6)
students.append(s7)
students.append(s8)
students.append(s9)

students.extend([s10])  #toplu eklemek için listeadı.extend([nesne1,nesne2...])
teachers.extend([t1,t2,t3,t4,t5,t6,t7])
employees.extend([e1,e2,e3])
# kisiler.append(t1)
# kisiler.append(t2)
# kisiler.append(t3)
# kisiler.append(t4)
# kisiler.append(t5)
# kisiler.append(e1)
# kisiler.append(e2)
# kisiler.append(e3)

# s1.getInfo()  
# s1.studentList(students)  #bir tane nesne üzerinden listeyi görüntülüyoruz
# t1.teacherList(teachers)
# e1.employeeList(employees)


Menu()