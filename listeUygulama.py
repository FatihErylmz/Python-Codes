#Uygulama Listeler
#1 Toyota Bmw , Renault,Mercedes elemanlarına sahip markalar adında bir liste oluşturun 
markalar=["Toyota","Bmw","Renault","Mercedes"]

#2 Oluşturulan Liste kaç elemanlıdır
sonuc= len(markalar) 
print(sonuc) #4

#3 Listenin ilk ve son elemanı nedir
print(markalar[0]) #Toyota
print(markalar[-1]) #Mercedes

#4 Renault markasını Togg ile değiştirin
markalar[2]= "Togg"

#5 Togg Listenin bir elemanımıdır   
sonuc="Togg" in markalar
print(sonuc)  #True

#6 Listenin ilk 2 elemanını aliniz 
sonuc= markalar[:2]

#7 Listenin sonuna "Ford" ve "Citroen" ekleyiniz
sonuc= markalar +["Ford", "Citroen"]

#8 Listenin son elemanını silin 
del markalar[-1]

#9 Aşağıdaki veerileri liste içerisinde saklayınız
#ogrenci1: Ertuğrul 2010 [70,80,90]
#ogrenci2: Tony 2011 [70,45,60]
#ogrenci3: David 2012 [30,95,50]

ogrenci1= ["Ertugrul", 2010,[70,80,90]]
ogrenci2= ["Tony", 2011,[70,45,60]]
ogrenci3= ["David", 2012,[30,95,50]]

ogrenciler=[ogrenci1,ogrenci2,ogrenci3]
print(ogrenciler) 

#10 Ogrencilerin yaslarını hesaplayınız 
yasErtugrul= 2024-ogrenciler[0][1]
yasTony= 2024-ogrenciler[1][1]
yasDavid= 2024-ogrenciler[2][1]
print(yasErtugrul,yasTony,yasDavid) #14 13 12 

#11 Ogrencilerin not ortalamalarını hesaplayınız 
notErtugrul= (ogrenciler[0][2][0] +  ogrenciler[0][2][1] +  ogrenciler[0][2][2] ) / 3
notTony= (ogrenciler[1][2][0] +  ogrenciler[1][2][1] +  ogrenciler[1][2][2] ) / 3
notDavid= (ogrenciler[2][2][0] +  ogrenciler[2][2][1] +  ogrenciler[2][2][2] ) / 3
print(notErtugrul,notTony,notDavid) 