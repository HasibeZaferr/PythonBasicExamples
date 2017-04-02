# -*- coding: utf-8 -*-

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # tuple içindeki tüm elemanları yazar.
print (tuple[0])        # tuple içindeki ilk elemanı yazar.
print (tuple[1:3])      # 2. elemandan 3. elemana kadar olanları yazar.
print (tuple[2:])       # 3. elemandan ve sonrasındaki bütün elemanları yazar.
print (tinytuple * 2)   # tinytuple içindeki elemanları iki kere yazar.
print (tuple + tinytuple) # tuple ve tinytuple içindeki elemanları birleştirerek yazar.

#Listeler ve tuple'ler arasındaki temel fark: listeler köşeli parantez içerisindedir []
# ve elemanları ve boyutu değiştirilebilir, ancak tuple parantez içine alınır () ve güncellenemez.