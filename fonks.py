#Göderilen bir kelimeyi belirtilen kez ekranda gösteren foks. yazın

def kelimeYazdir():
    kelime=input("Kelime yazın: ")
    defa=int(input("Kaç defa kelime yazsın:" ))
    i=0
    while i<defa:
        print(kelime)
        i+=1


kelimeYazdir()

#Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonks. yazın

def listeyeCevir(*params):  ## * tek yıldızda tuple tipi liste ** çift yıldızda dictionary belirttiğimiz anlamına gelir
    liste1=[]
    liste1.append(params)
    print(liste1)

listeyeCevir(1,2,3)

#Gönderilen 2 sayı arasındaki tüm asal sayıları bulun

def AsalBul():
    baslangic=int(input("Başlangıç değerini giriniz::" ))
    bitis=int(input("Bitis değerini giriniz::" ))
    sayi=baslangic
                    
    for i in range(baslangic,bitis):
        if(i<2):
            i+2


        for a in range(i):
            if(sayi%i!=0):
                i-=1
            else:
                break
        print(sayi)
        i+=1


        AsalBul()
    # Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonks yazın

   

    # def SayininTamBölenleri():
    #     sayi=int(input("Sayiyi giriniz::" ))
    #     for i in range(sayi):
    #         for i in range(sayi):
    #             if(sayi%i==0):
    #                 print(f"{sayi} nın tam bölenleri: ",end=" ")
    #                 print(i)
    #                 i-=1

    def SayininTamBölenleri():
        sayi=int(input("Sayiyi giriniz::" ))
        for i in range(1,sayi+1):
            
            if(sayi%i==0):
                print(f"{sayi} nın tam bölenleri: ",end=" ")
                print(i)
                  

    SayininTamBölenleri()