#sets: dizilerde tekrar eden elemanları siler.
#Listede zaten tekrar eden eleman olamaz
fruits={'orange', 'apple','banana'}
#süslü panatezlerle açılmış listeler indekslenemez listelerdir.
#indekslenemez olduğu için sıralayamayız.
# print(fruit[0]) #hata verir.indekslenemez
# elemanlarına ancak döngü ile ulaşılır

for x in fruits:
    print(x)


fruits.add('cherry') # eleman ekleme
print(fruits)
fruits.update(['mango', 'grape']) #liste ekledik update ile
print(fruits)
fruits.add('mango') #listeye eklenmez aynısı olduğu için
print(fruits)

myList=[1,2,3,4,4,3,2,1]
print(myList)
print(set(myList)) #tekrarlanan elemanlar silindi

fruits.remove('mango') #eleman silmek için
print(fruits)
fruits.discard('apple')#eleman silmek için
print(fruits)
fruits.pop() #pop normalde son elemanı siler ama elemanlar sıralanmadığı için herhangi bir elemanı siler
fruits.clear()  #tüm elemanlar silinir












