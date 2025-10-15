# # def squarw(num): return num**2
# # tek satırlık fonksiyonlarda return kullanımı opsiyonel

# numbers=[1,2,3,4]

# # result=list(map(square,numbers))  # map fonksiyonu verilen listeyi tek tek alır ve fonksiyona gönderir
# # # map ya listeye atanmalı ya da direk for döngüsü ile yazdırılmalı
# # for i in map(square,numbers):
# #     print(i)

# # print(result)

# result=list(map(lambda num: num**2,numbers))

# # num ı al karesini al num a ata demek
# # yaptığımız işlemi bir değişkene de atayabiliriz
# square=lambda num: num**2
# print(square(5))

# # lambda ekspression u genellikle map,filter,reduce gibi fonksiyonlarla kullanırız
# # filter fonksiyonu verilen listedeki elemanları tek tek alır ve fonksiy

# def check_even(num):
#     return num%2==0
# # result=list(filter(check_even,numbers))e gönderir
# # filter fonksiyonu true dönen elemanları alır false dönenleri atar
# print(result)


# result =list(filter(lambda num: num%2==0,numbers))
# print(result)

# # map metodu verilen listedeki her elemanı tek tek alır ve fonksiyona gönderir
# # filter metodu verilen listedeki elemanları tek tek alır ve fonksiyona gönder


from modulefinder import test


numbers=[1,2,3,4,5,6,7,8,9,10]
result=list(map(lambda num: num**2,numbers))
print(result)

#map ve filter fonksiyonları lazy evaluation yapar
#lazy evaluation=değerler ihtiyaç duyulana kadar hesaplanmaz
#eager evaluation=tüm değerler hemen hesaplanır
#map ve filter fonksiyonları python 3 te liste döndürmezler 
#bunun yerine map object ve filter object dönerler
#bu objeleri listeye çevirmek için list() fonksiyonu kullanılır 

# lambdalı ifadeyi değişkene de atayabiliriz
# square=lambda num: num**2
# print(square(5))

# def check_even(num):
#     return num%2==0

# result=list(filter(check_even,numbers))
# print(result)

check_even=lambda num: num%2==0
print(check_even(10))
result=list(filter(lambda num: num%2==0,numbers))
print(result)

# lambda expression lar genellikle map,filter,reduce gibi fonksiyonlarla kullanılı
# reduce fonksiyonu functools modülünde tanımlıdır
# from functools import reduce
# #reduce fonksiyonu verilen listedeki elemanları tek tek alır ve fonksiyona gönderir
# #reduce fonksiyonu bir önceki elemanın sonucunu bir sonraki elemanla toplar

# result=reduce(lambda x,y: x+y,numbers)
# print(result)
# #x bir önceki elemanın sonucunu y ise bir sonraki elemanı temsil eder
# result=reduce(lambda x,y: x*y,numbers)
# print(result)
# #x bir önceki elemanın sonucunu y ise bir sonraki elemanı temsil eder
# result=reduce(lambda x,y: x if x>y else y,numbers)
# print(result)
# #x bir önceki elemanın sonucunu y ise bir sonraki elemanı temsil eder
# result=reduce(lambda x,y: x if x<y else y,numbers)
# print(result)

# lambda tanımlanmamış fonksiyon demektir
#tek satırlık fonksiyonlarda return kullanımı opsiyoneldir  

global scobe
x="global x"
def fonksiyon():
    #local scobe
    global x  
    x="local x"
    print(x)

    # fonksiyonun içerşsşbde x tanımlanmışsa global değer localı etkilemez.
    # ama fonks. içerisinde x tanımlanmamış olsaydı global tanımı alacaktı


    name="global name"
    def greeting():
        name="çınar" #bu da yorum satırı olsaydı hem ada hem çınar o zaman global olanı alırdı.
        def hello():
            # name="ADA" # ada çık olsaydı ada yazardı. 
            print("hello "+name)

        hello()
    greeting()


    x=50
    def test():
        global x 
        print(f"x: {x} ")

        x=100
        print(f"fonksiyon içinde x: {x} ")

print(x)
print(test(x))