# String Uygulama
title = "Python ile Programlama"

# 1- title değişkeni içerisindeki karakter sayisi

print(len(title))  #22

#2 title içerisindeki python değişkenini alin 
print(title[:6]) #Python

#3 title değişkeninin ilk 5 ve son 5 karakterini alin
print(title[:6]) #Python
print(title[-5:]) #mlama

#4 title değişkenini tersten yazdırınız
print(title[::1]) #bastan birer karakter alarak yazdırır -->   # Python ile Programlama
print(title[::-1]) #sondan birer karakter -->  # amalmargorP eli nohtyP

# 5 Klavyeden girilen ögrenci bilgisine göre örnek verilen cümleyi yazdiriniz 
# 1. notu 60 2.notu 60 ve not ortalamasi 60 olarak hesaplanmıştır

puan1= input("puan ")
puan2= input("puan 2 ")
ort= (float(puan1)+float(puan2))/2    
sonuc= f"1.notu {puan1} , 2.notu {puan2} ve not ortalamasi {ort} olarak hesaplanmistir"
print(sonuc)