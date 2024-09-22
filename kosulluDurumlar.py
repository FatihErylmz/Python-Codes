#KOŞULLU DURUMLAR: UYGULAMA

# 1 Bir aracın yakıt tipine göre (benzin dizel lpg) belirtilen bir mesafede 
# ne kadar yakıt masrafı oldugunu hesaplayın

# benzin : 44.66
# dizel  : 44.79
# lpg    : 23.04

benzinFiyat = 44.66
dizelFiyat = 44.79
lpgFiyat = 23.04
toplamYakitUcreti=0

ortalamaYakitTuketimi = float(input("100 km / yakit tüketimi değeri "))
mesafeKm= float(input("  km "))
print("Örnek Yakit Tipleri: benzin lpg  dizel ")
YakitTipi = input("Yakit tipini girin ")

toplamYakitTuketimi = (mesafeKm*(ortalamaYakitTuketimi/100))
print(f"Toplam Tüketilen Yakit Miktari {toplamYakitTuketimi} Litre")

#Fiyat
if(YakitTipi=="benzin"):
    print(f"{round(toplamYakitTuketimi*benzinFiyat,2)} TL")

elif(YakitTipi=="dizel"):
    print(f"{round(toplamYakitTuketimi*dizelFiyat,2)} TL")

elif(YakitTipi=="lpg"):
    print(f"{round(toplamYakitTuketimi*lpgFiyat,2)} TL")

else:
    print("yakit tipi hatali")

    
    # 2 Bir öğrencinin 2 yazılı 1 proje notunu alarak ortalama hesaplayınız ve hesaplanan
#ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız
"""
0-24    0
25-44   1
45-54   2
55-69   3
70-84   4
85-100  5

"""
yazili1=float(input("1.Yazili notu "))
yazili2=float(input("1.Yazili notu "))
proje=float(input("1.Yazili notu "))

ortalama= (yazili1+yazili2+proje)/3

if(ortalama>=0) and (ortalama<25):
    print(f"ortalamaniz {ortalama} ve değerlendirme notunuz 0")

if(ortalama>=25) and (ortalama<45):
    print(f"ortalamaniz {ortalama} ve değerlendirme notunuz 1")

if(ortalama>=45) and (ortalama<55):
    print(f"ortalamaniz {ortalama} ve değerlendirme notunuz 2")

if(ortalama>=55) and (ortalama<70):
    print(f"ortalamaniz {ortalama} ve değerlendirme notunuz 3")

if(ortalama>=70) and (ortalama<84):
    print(f"ortalamaniz {ortalama} ve değerlendirme notunuz 4")

if(ortalama>=85) and (ortalama<=100):
    print(f"ortalamaniz {ortalama} ve değerlendirme notunuz 5")