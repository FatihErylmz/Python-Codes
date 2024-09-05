#LİSTELER
kurum = "BTK AKADEMİ".split() #str to list 

print(type(kurum)) #<class 'list'>
print(kurum[0]) #BTK
print(kurum[1]) #AKADEMİ

sayilar= [1,2,3,4,5]
isimler =["ali","ahmet"]
print(type(sayilar)) #<class 'list'>
print(type(sayilar[0])) # <class 'int'>

print(type(isimler)) #<class 'list'>
print(type(isimler[0])) # <class 'str'>

ogrenci=["Ertuğrul" , "Ali" , 60,50,70]
print(ogrenci[0] +" "+ ogrenci[1]) #Ertuğrul Ali

ortalama= (ogrenci[2] + ogrenci[3] + ogrenci[4]) / 3 
print(ortalama) #60.0

ogrenciler=[["Ertuğrul" , "Ali" , 60,50,70],["Tekin","Ali" , 80,90,70]]
print(ogrenciler[0]) #['Ertuğrul', 'Ali', 60, 50, 70]
print(ogrenciler[1]) #['Tekin', 'Ali', 80, 90, 70]

print(ogrenciler[0][0]) #Ertuğrul
print(ogrenciler[1][4]) #70