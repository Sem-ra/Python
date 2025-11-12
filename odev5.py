"""
open(path, mode, encoding="utf-8") 

'r' : okuma (read). Dosya yoksa hata verir.

'w' : yazma (write). Dosya varsa içeriğini siler, yoksa oluşturur.

'a' : ekleme (append). Dosya varsa sonuna yazar, yoksa oluşturur.

'x' : exclusive create — dosya varsa hata verir, yeni oluşturur.

'r+': okuma + yazma (dosyanın içeriğini korur).

'w+': yazma + okuma (önce dosyayı siler/yeniden oluşturur).

'a+': ekleme + okuma.

context manager --> with
with open("ornek.txt", "w", encoding="utf-8") as f:
    f.write("Merhaba\n")
# blok çikinca f.close() otomatik çağrilir.Oyüzden close demeye gerek yok. otomatik geliyor.

DOSYA OKUMA YÖNTEMLERİ
with open("ornek.txt", "r", encoding="utf-8") as f:
    # tüm içeriği tek bir string olarak:
    text = f.read()   # READ TÜM İÇERİĞİ OKUYOR

with open("ornek.txt", "r", encoding="utf-8") as f:
    # tek satır oku:
    first_line = f.readline()  #READLİNE TEK SATIR OKUYOR

with open("ornek.txt", "r", encoding="utf-8") as f:<
    # tüm satırları liste olarak:
    lines = f.readlines() #TÜM SATIRLARI LİSTE OLARAK

# daha verimli ve Pythonik: dosya üzerinde iterasyon (satır satır)
with open("ornek.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # TÜM SAYFAYI BOŞLUKTAN AYIRIP Kİ STRİPİN PARANTEZLERİNE NE YAZARSAK ONDAN AYIRARAK SATIR SATIR OKUYOR

DOSYA YAZMA YÖNTEMLERİ
with open("yeni.txt", "w", encoding="utf-8") as f:
    f.write("Bir satır\n")
    f.writelines(["satır2\n", "satır3\n"])  # listeden yazar (elemanlara otomatik newline eklemez)









with open("ToText.txt","w",encoding="utf-8") as f:
    f.write("Hello Guys\n") #f.write() dosyaya yazar, ekrana değil. print etsem ekrana string ifadenin len ini verir.
    f.writelines(["Hello Friends\n","Hello Heleluya\n"]) # writelines(["....\n","...\"])
    f.writelines(["hi guys\n","hi friends\n","hi heleluya\n"])

with open("ToText.txt","r",encoding="utf-8") as f: #Dosyayı okur, return eder ama sonucu bir değişkende saklamadık ve print etmedik.o yüzden ekranda bir şey gösterilmez
    a=f.read()
    print(a)
# çıktı:
# Hello Guys
# Hello Friends
# Hello Heleluya
# hi guys
# hi friends
# hi heleluya
#o halde önce w ile yazma modunda dosya oluşturduk. Dosya yoksa da hata vermedi oluşturdu. Writeın parantezleri içerisinde mesajımızı yazdık.
#Fakat write modunda print len döndürdüğü için yani karakter sayısını vereceği için ekrana çıktılamak istediğim metni okuma modunda açmam gerekiyor
#okuma modundan sonra  print edebiliyorum

# writelines() --->Liste veya iterable içindeki birden fazla stringi yazar.writelines(["....\n","...\"])
#writelines() “line” ismine rağmen satır sonuna \n (newline) eklemez.kendin ekleyeceksin,ekelmezsen bitişik olur
# write() ---> tek bir stringi yazar

#readlines() → dosyadaki her satırı bir liste elemanı olarak döndürür.
# #Satırların sonunda \n (yeni satır karakteri) hala durur çünkü Python bunları da okur.eer s\n istenmiyorsa strip yapılmalı
with open("ToText.txt", "r", encoding="utf-8") as f:
    satirlar = [satir.strip() for satir in f.readlines()]  # strip() boşluk ve \n siler
print(satirlar)

#çıktı-->['Hello Guys', 'Hello Friends', 'Hello Heleluya', 'hi guys', 'hi friends', 'hi heleluya']

with open("ToText.txt", "r", encoding="utf-8") as f:
    print(f.read())  --> dosya yolu çalışıyor mu test etmek için



"""



# # # # @staticmethod # bunu yaptığımda self eklememe gerek kalmıyor
# class Student:
#     students=[]
#     def __init__(self,studentId,name,surname):
#         self.studentId=studentId
#         self.name=name
#         self.surname=surname

#         Student.students.append(self) #nesne oluştuğunda örenciler otomatik eklenecek

#     def studentsAdd(self):
       
#         while(True):
#             try:
#                 Id=int(input("Id:"))
#             except(ValueError)as e:
#                 print("Invalid Input.Please enter numbers only!", e)
#                 continue
#             try:
#                 name=input("name: ")  #isalpha string kontrolü yapıyor
#                 if not name.isalpha():
#                     print("Name must contain letters only.")
#                     continue
#                 surname=input("Surname: ")
#                 if not name.isalpha():
#                     print("Surname must contain letters only.")
#                     continue
#             except:
#                 print("Invalid input")
#                 continue
#             new_student=Student(Id,name,surname)
#             with open(r"C:\Users\HP\OneDrive\Masaüstü\ogrenciler.txt", "a", encoding="utf-8") as f:
#                  f.write(f"{new_student.studentId},{new_student.name},{new_student.surname}\n")
#             print("Student add")
            
#             answer=input("Do you want to continue. yes/no: ").lower()
#             if(answer=="no"):
#                 break
        

# # stu1=Student("\n10","semra","cebeci")
# # stu1.studentsAdd()
# # Student.stundets.clear()

# # for i in Student.students:
# #     print(i.studentId,i.name,i.surname)

# # file = open(r"C:\Users\HP\OneDrive\Masaüstü\ToText.txt", "w", encoding="utf-8")
# # for i in Student.students:
# #      file.write(f"{i.studentId},{i.name},{i.surname}\n")
# # file.close()
# # try:
# #     with open(r"C:\Users\HP\OneDrive\Masaüstü\ogrenciler.txt","r",encoding="utf-8") as f:
# #     # print(f.read()) #dosya yolu çalışıyor mu test ettik. #hem read hem readlines olmaz. read ile satır sonuna kadar okur lines işleme alınacağı zaman boş döner çünkü satır sonunda
# #         icerik=f.readlines() #liste dönüyor ama boşluk karakteri var
# #         print(icerik) 
# # except Exception as ex:
# #     print("file not found",ex)

# try:
#     with open(r"C:\Users\HP\OneDrive\Masaüstü\ogrenciler.txt","r",encoding="utf-8") as f:
#         satirlar = [satir.strip() for satir in f.readlines()]
#         print(satirlar) #liste döndü boşluk karakteri yok
#     for satir in satirlar:
#         parts = satir.split(",")
#         if len(parts) == 3:
#             try:
#                 student_id = int(parts[0])  # sadece geçerli id al
#                 name = parts[1]
#                 surname = parts[2]
#                 Student(student_id, name, surname)
#             except ValueError:
#                 print(f"Hatalı satır atlandı: {satir}")
# except Exception as ex:
#     print("file not found",ex)

# sorted_students = sorted(Student.students, key=lambda s: int(s.studentId))
# for s in sorted_students:
#     print(s.studentId, s.name, s.surname)




    

# # # for satir in icerik.splitlines():
# # #     print(satir)
# # # \U, \M, \t gibi karakterleri özel kaçış (escape) olarak algılıyor (örneğin \t = tab boşluğu). o yüzden r (raw string) kullan:
# # file = open(r"C:\Users\HP\OneDrive\Masaüstü\ToText.txt", "w")

# file=open("dosya.txt","w",encoding="utf-8") #write
# a=file.write("Merhaba")
# file.close()





# def abc():
#     file=open("dosya.txt","w",encoding="utf-8") #write mod #üzerine yazıyor.
#     file.write("Hey\n")
#     file.write("Nasılsın?")
#     file.write("Nasılsın?")
#     file=open("dosya.txt","r",encoding="utf-8") #read mod
#     a=file.read()
#     print(a)
# abc()
# with open("dosya13.txt","a",encoding="utf-8") as file:
#     file.write("selam\n")
#     file.write("şğöğ")
#     file=open("dosya.txt","r",encoding="utf-8") #read mod
#     a=file.read()
#     print(a)

# def abd():
#     file=open("dosya.txt","w",encoding="utf-8")
#     file.write("\nbirikiüç")
#     file=open("dosya.txt","r",encoding="utf-8") #read mod
#     a=file.read()
#     print(a)

# abd()
    




def abc():
    file=open("dosya.txt","w",encoding="utf-8") #write mod #üzerine yazıyor.
    file.write("Hey\n")
    file.write("Nasılsın?\n")
    file.write("Nasıl yan?\n")
    file.write("nenene\n")

    file=open("dosya.txt","r",encoding="utf-8") #read mod
    a=file.read(80)
    print(a)
    for i in file:
        print(i)
        
abc()






