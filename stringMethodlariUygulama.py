#STRING Uygulama 2 
kurs_adi= "Btk akademi python ile programlama dersleri"
website= "https://www.btkakademi.gov.tr/"

# 1  Btk akademi karakter dizisinin başındaki ve sonundaki boşlukları siliniz
sonuc= 'Btk akademi'.strip()

#2 kurs_adi degiskeninin tüm harflerini kücük harfe cevir.
sonuc=kurs_adi.lower()

#3 website değişkeninde kaç tane '.' karakteri var
sonuc=website.count('.')

#4 website değişkeni https ile mi başlıyor
sonuc= website.startswith('https') 

#5 website değişkeni tr ile mi bitiyor
sonuc= website.startswith('tr') 

#6 kurs_Adi içerisindeli tüm karakterler harften mi olusuyor
sonuc= kurs_adi.isalpha()

#7 kurs_Adi içerisindeli tüm boşlukları - ile degistirin
sonuc= kurs_adi.replace(' ', '-')

#8 kurs_Adi içerisindeli python kelimesini degistir
sonuc= kurs_adi.replace('Python', 'A')

#9 website değişkeni www içeriyor mu 
sonuc= website.find('www')
sonuc=website.index('www')
# Değer bulunamazsa find() yöntemi -1 değerini döndürür.

#10 kurs_Adi degiskenini listeye cevir 
sonuc= kurs_adi.split()

print(sonuc)