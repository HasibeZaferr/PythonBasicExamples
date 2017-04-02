# -*- coding: utf-8 -*-

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#Dictionary tanımlanması

print ("dict['Name']: ", dict['Name'])
#Anahtar-deger(key-value) ilişkisiyle Name anahtarına ait değerin yazdırılması
print ("dict['Age']: ", dict['Age'])
#Anahtar-deger(key-value) ilişkisiyle Age anahtarına ait değerin yazdırılması
print ("dict['Class']:", dict['Class']);
#Anahtar-deger(key-value) ilişkisiyle Class anahtarına ait değerin yazdırılması


#Dictionary Güncelleme
dict['Age'] = 8; # Age 8 olarak güncellendi
dict['Name'] = "John" # Name John olarak güncellendi
print ("dict['Age']: ", dict['Age'])
print ("dict['Name']: ", dict['Name'])


#Dictionary Silme İşlemi
del dict['Name'] # Name anahtar-deger siler
dict.clear()     # Sözlükteki tüm girdileri kaldırır
del dict         # Sözlüğü siler

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
#Bir anahtara birden fazla değer atandığında son değer geçerli olur
print ("dict['Name']: ", dict['Name']) # dict['Name']:  Manni yazdırır


