"""Inheritance(Kalıtım): Miras Alma
# Bir class ın özelliklerini başka bir class a aktarmak için kullanılır.

Person=>  name, lastame,age,eat(),run()
Strudent(Person) , Teacher(Person)
person class ının tüm özelliklerini student ve teacher class ları kullanabilir.
ama person student ve teacher class larının özelliklerini kullanamaz.

Animal> dog(Animal), cat(Animal) 
dog ve cat animaldan miraz alır






"""

# class Person():
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         print("Person created")

#         def who_am_i(self):
#             print("I am a person")  
#         def eat(self):
#             print("I am eating")

# class Student(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname) #person ın init methodunu çağırdık    
#         print("Student created")

#        #override  temel classın methodunu değiştirme
#     def who_am_i(self):
#         print("I am a student")

# class Teacher(Person):
#     def __init__(self,fname,lname,branch):
#         super().__init__(fname,lname)
#         print("Teacher created")
#         self.branch=branch


# p1=Person("Ali","Yilmaz")
# s1=Student( "Veli","Demir")

# print(p1.fname+ " "+p1.lname)
# print(s1.fname+ " "+s1.lname)

# p1.who_am_i()
# s1.who_am_i()

# class Movie():
#     def __init__(self,title,director,duration):
#       self.title = title
#       self.director = director
#       self.duration = duration
#       print("Movie created")
    
#     def __str__(self):
#         return f"{self.title} by {self.director}"
    
#     def __len__(self):
#         return self.duration
#     def __del__(self):
#         print("Movie object deleted")
        

# m=Movie("fil ad","yonetmen ad",120 )
# print(str(m))
# print(len(m))

#quiz ve question classları olacak
#question listesi alacağız.
#toplam soru sayısı ve kaçıncı soruda olduğunu göstereceğiz
#skor tutucaz her doğru soru 1 puan
#skoru quiz bitince yazdırcaz

class Question:
    def __init__(self, text, chooses, answer):
        self.text = text
        self.chooses = chooses
        self.answer = answer    

q1 = Question("En iyi yazılım dili1?", ["c#", "javascript", "java", "python"], "python")
q2 = Question("En iyi yazılım dili2?", ["c#", "javascript", "java", "python"], "python")
q3 = Question("En iyi yazılım dili3?", ["c#", "javascript", "java", "python"], "python")
q4 = Question("En iyi yazılım dili4?", ["c#", "javascript", "java", "python"], "python")
q5 = Question("En iyi yazılım dili5?", ["c#", "javascript", "java", "python"], "python")

questions = [q1, q2, q3, q4, q5] 

class Quiz:
    #contructor(kurucu metot)
    def __init__(self, questionListesi):
        self.questions = questionListesi
        self.questionIndex = 0
        self.score = 0

    def soruyuGetir(self):
        denemeSorusu = self.questions[self.questionIndex]
        print(f"{self.questionIndex +1 } of {len(self.questions)} \n{denemeSorusu.text}")
        for chooses in denemeSorusu.chooses:
            print (f"- {chooses}")        


    def cevapKontrol(self, girilenCevap):
        denemeCevabi = self.questions[self.questionIndex]
        dogruMu = girilenCevap == denemeCevabi.answer
        return (dogruMu)
    
    def cevapSonrasi(self, a):        
        if (Quiz.cevapKontrol(self, a) == True): self.score += 1
        if (self.questionIndex < len(self.questions)):
            self.questionIndex += 1
        if (self.questionIndex == len(self.questions)):            
            print(f"Sınav bitti \nSkorunuz: {self.score}")            
        

    
    def displayScreen(self):
        Quiz.soruyuGetir(self)
        a = input("Cevabınızı yaziniz: ")
        Quiz.cevapSonrasi(self, a)        
        if (self.questionIndex < len(self.questions)):
            Quiz.displayScreen(self)
        
        

sinav = Quiz(questions)
sinav.displayScreen()#quiz ve question classları olacak
#question listesi alacağız.
#toplam soru sayısı ve kaçıncı soruda olduğunu göstereceğiz
#skor tutucaz her doğru soru 1 puan
#skoru quiz bitince yazdırcaz

class Question:
    def __init__(self, text, chooses, answer):
        self.text = text
        self.chooses = chooses
        self.answer = answer    

q1 = Question("En iyi yazılım dili1?", ["c#", "javascript", "java", "python"], "python")
q2 = Question("En iyi yazılım dili2?", ["c#", "javascript", "java", "python"], "python")
q3 = Question("En iyi yazılım dili3?", ["c#", "javascript", "java", "python"], "python")
q4 = Question("En iyi yazılım dili4?", ["c#", "javascript", "java", "python"], "python")
q5 = Question("En iyi yazılım dili5?", ["c#", "javascript", "java", "python"], "python")

questions = [q1, q2, q3, q4, q5] 

class Quiz:
    #contructor(kurucu metot)
    def __init__(self, questionListesi):
        self.questions = questionListesi
        self.questionIndex = 0
        self.score = 0

    def soruyuGetir(self):
        denemeSorusu = self.questions[self.questionIndex]
        print(f"{self.questionIndex +1 } of {len(self.questions)} \n{denemeSorusu.text}")
        for chooses in denemeSorusu.chooses:
            print (f"- {chooses}")        


    def cevapKontrol(self, girilenCevap):
        denemeCevabi = self.questions[self.questionIndex]
        dogruMu = girilenCevap == denemeCevabi.answer
        return (dogruMu)
    
    def cevapSonrasi(self, a):        
        if (Quiz.cevapKontrol(self, a) == True): self.score += 1
        if (self.questionIndex < len(self.questions)):
            self.questionIndex += 1
        if (self.questionIndex == len(self.questions)):            
            print(f"Sınav bitti \nSkorunuz: {self.score}")            
        

    
    def displayScreen(self):
        Quiz.soruyuGetir(self)
        a = input("Cevabınızı yaziniz: ")
        Quiz.cevapSonrasi(self, a)        
        if (self.questionIndex < len(self.questions)):
            Quiz.displayScreen(self)
        
        

sinav = Quiz(questions)
sinav.displayScreen()
