#STRING METHODLARI

mesaj= "btk akademi Python Kursu"

sonuc= mesaj.upper()  # BTK AKADEMİ PYTHON KURSU
sonuc= mesaj.lower()  # btk akademi python kursu
sonuc = mesaj.title() # Btk Akademi Python Kursu  Tüm kelimelerin baş harfleri büyük
sonuc = mesaj.capitalize() # Btk akademi python kursu  Sadece ilk kelimenin baş harfi büyük
 
sonuc = "abc".islower()  # True --> kücük harf mi ?
sonuc = mesaj.strip()    #Baştaki boşluk karakterini siler
sonuc = mesaj.split()  #  default tüm karakterleri bosluktan ayırır liste yöntemi  ['btk', 'akademi', 'Python', 'Kursu']
sonuc = mesaj.split(",")  # virgülden ayırır 
sonuc = mesaj.index("akademi")  # akademi kelimesi hangi indexten başlıyor # 4 
sonuc = mesaj.startswith("b")  #  bu liste b ile mi başlıyor #True
sonuc = mesaj.endswith("u")  #  bu liste u ile mi bitiyor #True
sonuc= mesaj.replace("Python" , "Javascript")  #btk akademi Javascript Kursu
print(sonuc)