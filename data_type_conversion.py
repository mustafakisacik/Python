# -*- coding: utf-8 -*-
"""
Created 

@author: MUSTAFA
"""
#tam sayiyi ondalikli sayiya cevirmek icin float() fonksiyonunu kullaniriz.
a=13
print(a) # a degerini yazdirdik 

b=float(a) # a degerini float'a cevirdik ve b'ye atadik.
print(b) # b degerini yazdirdik

c=float(-a) # eksi a degerini float yaptik ve c'ye atadik.
print(c) 

#ondalikli sayiyi tam sayiya cevirmek icin int() fonksiyonunu kullaniriz.

d=14.98557741213
e=int(d)
f=int(-d) 
print(e)
print(f)

#bir sayiyi stringe cevirmek icin str() fonksiyonunu kullaniriz.
p=3.14159265
i=str(p) # p degerimizi string yapip, i'ye atadik.
print(i) # i degerimizi yazdirdik.
print(type(i)) # i degerimizin veri tipini yazdirdik.

uzunluk=len(i) # i degerimizin uzunlugunu bulmak icin len() fonksiyonumuzu kullaniyoruz.
print(uzunluk) # uzunlugumuzu yazdirdik.

# \n ve \t kullanimi

print("Merhaba Değerli Python Öğrencisi, \nNasılsın?") # \n alt satira geçmemizi sağlıyor.
print("X\tY\tZ\t") # \t tab kadar bosluk birakir.

print(type(3.14159265)) # veri tipini yazdirdik.


# sep parametresi yazdirdigimiz degerlerin arasina istedigimiz isaretleri koymamızı saglıyor.
print(1,2,3,4,5,sep='.')
print("14","12","20",sep="/")

print(*"MUSTAFA") # * işareti ile tırnak içinde olanlar birer boşluk arayla yazdirilir.


# format fonksiyonumuz ile istediğimiz değerleri "{}" içlerine yerleştirebiliriz. 
a=3
b=4
print("{} {} {}".format(a,b,a+b))

print("{}+{}'nın toplamı {}'dır.".format(a,b,a+b))

print("{2} {0} {1}".format("Kısacık", 24, "Mustafa"))

print("{:.2f} {:.3f} {:.4f}".format(2.345741, 8.54502, 6.321420))

class test(object):

    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'test'
    
print('{:open-the-pod-bay-doors}'.format(test()))

#https://pyformat.info/ adresinden daha detaylı bakabiliriz.



