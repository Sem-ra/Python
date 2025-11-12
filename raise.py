x=10
if x > 5:
    raise Exception("x 5 ten büyük değer alamaz")

#raise ile hatayı biz belirliyoruz

def check_pasword(psw):
    import re
    if len(psw) <8:
        raise Exception("en az 7 karakter")
    elif not re.search("[a-z]",psw):
        raise Exception("paralo küçük harf içermelidir")
    elif not re.search("[A-Z]",psw):
        raise Exception("paralo büyül harf içermelidir")
    elif not re.search("[0-9]",psw):
        raise Exception("paralo rakam içermelidir")
    elif not re.search("[_@$]",psw):
        raise Exception("paralo alpha numeric karakter içermelidir")
    elif  re.search("\s",psw):
        raise Exception("paralo boşluk içermemeli")
    else:
        print("geçerli paralo: else")
    # Finally:
    # print("tamamlandı")









