"""
for i in range(4, -1, -1):
    print(i)

4 → başlangıç değeri

-1 → bitiş değeri (dahil değil)

-1 → her adımda 1 azalt anlamına gelir.
for i in range(başlangıçdeğeri,bitiş,kaçarazalacak)
"""




sayilar=[1,3,5,7,9,12,19,21]

# SORU1) LİSTEDEKİ 3 ÜN KATI SAYILAR
for i in sayilar:
    if(i%3==0):
        {print(i)}

# SORU2) LİSTEDEKİ SAYILARIN TOPLAMI
toplam=0
for i in sayilar: 
    toplam+=i     
print(toplam)

# SORU3) LİSTEDEKİ TEK SAYILARIN KARESİ
for i in sayilar:
    if(i%2==1):
       print( i*i)

# SORU4) ŞEHİRLERİN HANGİLERİ EN FAZLA 5 KARAKTERLİDİR
sehirler=["kocaeli", "istanbul", "ankara","izmir","rize"]
for i in sehirler:
    if(len(i) <=5):
        print(i)
#SORU 5,6 

urunler = [{"name": "samsung s6", "price": "3000"},
           {"name": "samsung s7", "price": "4000"},
           {"name": "samsung s8", "price": "5000"},
           {"name": "samsung s9", "price": "6000"},
           {"name": "samsung s10", "price": "7000"}] 
# 5) ÜRÜNLERİN FİYATLARI TOPLAMI NEDİR
    # print(users["cinarturan"]) #cinarturanın bilgileri
toplam=0
for item in urunler:
    toplam+=int(item["price"])
print(toplam)

# 6)ÜRÜNLERİN FİYATI EN FAZLA 5000 OLAN ÜRÜNLERİ GÖSTERİNİZ.
for item in urunler:
    if(int(item["price"])<=5000):
        print(item)


name=""  #Python’da boş string ("") false kabul edilir
while not name: #true olunca duracak
    name=input("isminizi giriniz: ")
print(f"merhaba, {name}")