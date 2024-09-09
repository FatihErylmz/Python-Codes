#Liste Methodları
sayilar=[4,6,8,2,56,78,90]
isimler=["ahmet","canan","zeynep","gökhan"]
sonuc= min(sayilar)
print(sonuc)  #2

sonuc= max(sayilar)
print(sonuc)  #90

sonuc= min(isimler)
print(sonuc)  #ahmet

#ekleme Listenin sonuna
sayilar.append(12)
sonuc=sayilar
print(sonuc) #[4, 6, 8, 2, 56, 78, 90, 12]

isimler.append("ertuğrul")
sonuc=isimler
print(sonuc) #['ahmet', 'canan', 'zeynep', 'gökhan', 'ertuğrul']

#istediğimiz konuma ekleme
sayilar.insert(0,100) # 0. indekse 100 ekle  elemanları saga kaydırır
sonuc=sayilar
print(sonuc) #[100, 4, 6, 8, 2, 56, 78, 90, 12]

sayilar.insert(-1,500) # bir sag kaydırıp oraya ekliyor son eleman 500 olmayacak
sayilar.insert(-3,600) # bir sag kaydırıp oraya ekliyor son eleman 500 olmayacak
print(sonuc) #[100, 4, 6, 8, 2, 56, 78, 600, 90, 500, 12]
sayilar.insert(len(sayilar),700) # listenin son indexi
print(sonuc) #[100, 4, 6, 8, 2, 56, 78, 600, 90, 500, 12, 700]

#silme
sayilar.pop() # son indexteki elemani siler
sonuc=sayilar
print(sonuc) #[100, 4, 6, 8, 2, 56, 78, 90, 12]
sayilar.pop(0)
print(sonuc) #[4, 6, 8, 2, 56, 78, 600, 90, 500, 12]

isimler.remove('zeynep')
sonuc=isimler
print(isimler) #['ahmet', 'canan', 'gökhan', 'ertuğrul']

#sıralama 
sayilar.sort() #[2, 4, 6, 8, 12, 56, 78, 90, 500, 600]
sayilar.reverse() #[600, 500, 90, 78, 56, 12, 8, 6, 4, 2]
sonuc=sayilar
print(sonuc)  

# kac adet var ? 
sonuc= isimler.count("ertuğrul")
print(sonuc) #1

#arama
sonuc= sayilar.index(6)
print(sonuc) #7.indexte