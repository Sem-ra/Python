with open("newfile.txt","r",encoding="utf-8") as file:
    content=file.read() # read(10) ilk 10 tanesini oku demek
    print(content)
    file.seek(0) #cürsör ü 0. konuma gönderdik
    #with ile başladığımızda kapatmaya gerek kalmıyor kendisi kapanıyor kodlar bitince

print(file.tell()) # cürsör in konumunu verir imlecin

content2=file.read()
print(content2)
