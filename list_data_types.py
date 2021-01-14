# -*- coding: utf-8 -*-
"""
@author: MUSTAFA
"""
""" liste değişkenimizde, değişik veri tipinde veriler saklayabiliyoruz. """

liste = [1,2,3,4,"Elma",3.14159265,5.4321]
print(liste)
print(len(liste))  #liste uzunluğu
print(type(liste)) #veri tipi

liste1 = list() #boş liste oluşturma fonksiyonu 
print(liste1)

liste2=list("MUSTAFA") #list fonksiyonun içine string yazarsak, liste oluşturur.
print(liste2) #list fonksiyonundaki stringin her karakterini ayrı ayrı yazdıracak.

"""listeleri indeksleme ve parçalama"""
print(liste2[3])   # 3.indekste olan karakteri verir.
print(liste2[-2])  # sondan başlayarak 2.indekste olan karakteri verir.
print(liste2[0:4]) # 4'e kadar olan indeksleri yazdırırız.
print(liste2[2:])  # 2.indeksten başlayarak 
print(liste2[:6])
print(liste2[3])


a=liste[len(liste) -2] # listenin sondan ikinci elemanını gösterir.
print(a)  # matemaktiksel formu; L[len(L)-1]

print(liste[4:]) # listemizde 4.indeksten başlayıp sona kadar olan değerleri alır.
print(liste[:6]) # listemizde baştan başlayıp 6.indekse kadar olan değerleri alır.
print(liste[::3])# listeyi üçer üçer atlayarak okuruz.
print(liste[::-2]) # listeyi sondan başlayarak, ikişerli atlayarak okuruz. ve listeyi tersine çevirebiliriz.

"""Temel Lİste metotları ve işlemler"""
liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10]
print(liste1+liste2)  # listelerde toplama(birleştirme) işlemi
print(liste1*3) # liste1 üç kez yazdırıyoruz.

list1 = [8,5,2,4,9]
list1[2] = 0
print(list1) # list1 isimli listemizin 2.indeksindeki değeri değiştirdik.

list1[0:3] = [15,16,17] #list1 isimli listemizin ilk üç indeksindeki değeri değiştirdik.
print(list1)

"""Methodlar"""
liste.append("Python") #append metodu verdiğimiz değeri listemize eklemeyi sağlar. 
print(liste)

liste.append(10)
print(liste)

liste.pop(4) # pop metodu ile listemizden istediğimiz değeri çıkartabiliriz. 
print(liste)

print(liste.pop())
print(liste)

numbers = [1, 4, 3, 2] # https://www.geeksforgeeks.org/python-list-sort/
numbers.sort() 
print(numbers)

liste = ["Java", "Python", "Matlab", "C"] #alfabetik olarak sıralanır.
liste.sort() 
print(liste)

liste.sort(reverse=True) #alfabetik olarak tersten sıralanır.
liste.sort() 
print(liste)


liste = [[1,2],[2,8],[3,0],[5,7]] 
print(liste) 
print(liste[1])
print(liste[1][0])
print(liste[1][1])

print(liste[3])
print(liste[3][0])
print(liste[3][1]) #listenin içindeki değerlere ulaşabiliriz.


print(liste[20]) #listede olmayan bir indeksi yazdırmaya çalışırsak, list index out of range hatası alırız.




