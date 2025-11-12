class Student:
    def _init_(self, student_id, name, surname):
        self.student_id = student_id
        self.name = name
        self.surname = surname

students = []
sorted_students = []

def OgrenciKaydet(dosyaAdi):
    global sorted_students

    with open(dosyaAdi, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            
            if len(parts) >= 3:
                student_id = int(parts[0])
                name = parts[1]
                surname = parts[2]
                
                student = Student(student_id, name, surname)
                students.append(student)   
                sorted_students = sorted(students, key=lambda s: s.student_id)             
    
    for student in sorted_students:    
        print(f"{student.student_id}, {student.name}, {student.surname}")

def OgrenciSave():
    with open('ogrenciler_cikti.txt', 'w', encoding='utf-8') as file:         

        for student in sorted_students:
            line = f"{student.student_id:<5} {student.name:<15} {student.surname}\n"
            file.write(line)

def dosyaYoluGosterme():
    kacKere = int(input("kaç kere dosya giriceksiniz: ")) 
        
    for i in range(0, kacKere):
        dosyaAdiDeneme = input("hangi dosyadan öğrenci verisi yüklemek istiyorsunuz")
        OgrenciKaydet(dosyaAdiDeneme)

    # Sıralama OgrenciSave fonksiyonu içinde yapılıyor
    OgrenciSave()

dosyaYoluGosterme()