__author__ = 'sakkas'


#Fonksiyon tanımlarken aşağıdaki gibi tanımlanmalıdır.
#def fonksiyon_adı():
#   kodlar


#hello()# Fonksiyon aşağıda tanımlandığından 'hello' tanımlanmadı şeklinde hata verir
#Nu yüzden üstte tanımladıktan sonra aşağıda çağırıyoruz

def hello():
    print("Hello World")

hello()





#Parametre olarak aldığı sayının asal olup olmadığını bulan fonksiyon
def isPrime(num1):
    if num1 < 2:
        return False
    else:
        for i in range(2, num1):
            if num1 % i == 0:
                return False
        return True


num = eval(input("Bir sayı girin:"))
if isPrime(num):
    print(num, " bir asay sayı")
else:
    print(num, " bir asay sayı değil")
