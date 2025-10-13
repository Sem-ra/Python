#Tuple Listeleri:
#(tüpıl diye okunuyor)

list=[1,2,3,] # köşeli panatezler ile liste tanımladık
tuple=1,'iki',3 # şeklinde de yazılır. okunurluğu kolaylaştırmak için paranteze de alınır
tuple=(1,'iki',4)
print(type(list))
print(type(tuple))
print(list[0]) #0. indeksine eriştik
print(tuple[0])

#her ikisinde de len i kullanabiliriz

list=['ali','veli']
tuple=('damla','ayşe',"ayşe")
print(list,tuple)
#Burada listeki tüm elemanlar silinip yerilerine yukarıda yazılan elemanlar gelir. Her ikisi içinde geçerli bu. hem liste hem de tuple için
# Listenin herhangi bir indeksindeki elamana yeniden atama yapılırken tuple da index üzerinden herhangi bir değişiklik yapılamaz
list[0]="merve"
# tuple[0]="deli" # bu hata verir
print(list)
#tuple ın elemanları atandıktan sonra herhangi bir elemanı değiştirilemiyor. Ancak tüm liste silinip atama yapılabiliniyor
#yani sadece toptan atama işlemine yapılabiniyor.

print(tuple.count('ayşe')) #burada tuple da kaç tane ayşe var diye sorduk
print(tuple.index('ayşe')) #ayşe nin index nosuna ulaştık. iki tane var. ilk karşılaştığı index no döner
names=("en","güzel","hikayem") + tuple
print(names) #tuple emanları listeye eklendi





