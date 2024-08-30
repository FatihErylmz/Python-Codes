#VERİ TİPLERİ 
ad="Ertuğrul"
yas = 2
kilo = 12.1
ogrenciMi= False

#veri tipini ögrenmek için
print(type(ad))
print(type(yas))
print(type(kilo))
print(type(ogrenciMi))

print("ad " + ad + " yas " +str(yas) + " kilo " +str(kilo) +" Ogrenci mi " + str(ogrenciMi))

#VERİ TİPİ DÖNÜŞÜMÜ
sayi1= int(input("sayi 1: ")) 
sayi2= int(input("sayi 2: ")) 
toplam = sayi1+sayi2
print(toplam)  

x = int("10")
print(x) #10

# x1 = int("10.5") #hata

x1= int(10.5)
print(x1) #10

x2 = float("10")
print(x2) #10.0

x3= float(10)
print(x3) #10.0

x4 = float("10.4")
print(x4) #10.4

x5= str("3.4")
print(x5) # 3.4

x6= str(True)
print(x6) # True