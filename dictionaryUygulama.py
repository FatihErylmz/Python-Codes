# DICTIONARY: UYGULAMA
# 1 Verilen ogrenci bilgilerini dictionary listesinde saklayınız

"""
101 Fatih 2011 (40,80,90)
102 Hüseyin 2012 (80,80,80)
103 Ertuğrul 2017 (70 70 70)

"""
ogrenciler = {
    101:{         #101 key
    "numara": "101" ,
    "ad" : "Fatih" ,
    "tarih" : 2011 ,
    "puan" : (40,80,90)
     },
    
    102:{
    "numara": "102" ,
    "ad" : "Hüseyin" ,
    "tarih" : 2012 ,
    "puan" : (80,80,80)  
     },
     
     103:{
    "numara": "103" ,
    "ad" : "Ertuğrul" ,
    "tarih" : 2017 ,
    "puan" : (70,70,70)
         
    }

 }

#2 Klavyeden girilen ogrencı numarasına göre cümleyi yazdiriniz
# 101 numaralı Ertuğrulismindeki öğrencinin yaşı 7 ve not ortalaması 70
ogrenciNo = int(input('Ogrenci No '))
# print(ogrenciler[ogrenciNo]) 
#101 girersek sonuc --> {'numara': '101', 'ad': 'Fatih', 'tarih': 2011, 'puan': (40, 80, 90)}

# 101 numaralı Ertuğrul ismindeki öğrencinin yaşı 7 ve not ortalaması 70 istenen  bu ;

ogrenci= ogrenciler[ogrenciNo]

notOrtalama= (ogrenci["puan"][0] +ogrenci["puan"][1] +ogrenci["puan"][2]) / 3

print(f"{ogrenciNo} numarali {ogrenci["ad"]} ismindeki ogrencinin yaşı {2024-ogrenci["tarih"]}ve not ortalamasi {notOrtalama}")