
# #error==> hata
# #hataları önceden öngörüp önlem almalıyız
# #oalsı hatalar
# #tanımlanmamış bir değerin yazdırılması
#  hata çeliştleri
# #print(a)                 nameerror

# print('1a2')  valueror #tür hatası

# print(10/a)  zerodivisionError
#  print('denem'e)  syntaxeror



# Exception hiearchy  python.org/3/librarry/Exceptions.html


#Error Handling
# #error handlig => hata yönetimi
try:
    x=int(input("x:"))
    y=int(input("y:"))
except ZeroDivisionError:
    print("y sıfır girilemez")

try:
    x=int(input("x:"))
    y=int(input("y:"))
except ValueError:
    print(" x ve ye için sayısal değer girmelisiniz")

try:
    x=int(input("x:"))
    y=int(input("y:"))
except(ZeroDivisionError,ValueError)as e:
    print("hatalı giriş yaptınız")
    print(e)

try:
    x=int(input("x:"))
    y=int(input("y:"))
except:
    print("yanlış bilgi girdiniz")
else:
    print("her şey yolunda")

while True:
    try:
        x=int(input("x:"))
        y=int(input("y:"))
    except Exception as ex:
        print("yanlış bilgi girdiniz ",ex)
    else:
        break
    finally:
        print('try except sonlandı')
#finally her zaman çalışır.except ya da try bloğu çalışıp çalışmaması farketmeksizin
#finally bloğunun çalıştırılmasının mantığı bir dosya açtık onu kapatmamız gerekir onu da bu finally kısmında yapmış oluyoruz.








