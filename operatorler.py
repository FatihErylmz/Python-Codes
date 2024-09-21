#OPERATOR

#Aritmetik Operatorler
a=9
b=2

islem= a + b # 11
islem= a - b # 7
islem= a * b # 18
islem= a / b # 4.5
islem= a % b # 1
islem= a ** b # 81
islem= a // b # 4 

print(islem)

#ATAMA OPERATORLERI UYGULAMA

a,b,c= 4,8,(12,2)

# 1 Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı
sayi1 = int(input("sayi1: ")) #30
sayi2 = int(input("sayi2 "))  #20
carpim = sayi1*sayi2  #600
toplam= a + b +(c[0] + c[1]) #24

sonuc= carpim - toplam # 600-24 = 574
print(sonuc) # 574 

# 2 c  nin b ye kalansız bölümünü hesaplayınız 
sonuc=(c[0]+ c[1]) // b
print(sonuc) #1

#3 (a,b,c) toplamının mod 7 si nedir?
sonuc=(a+b+(c[0]+c[1])) % 7 

#4 b nin a. kuvvetini hesaplayın
sonuc = b**a

#5 a ,*b , c =(2,4,6,8,13) işlemine göre c nin küpü nedir
a ,*b , c =(2,4,6,8,13)
print(a,b,c) # 2 [4, 6, 8] 13
print(c**3) #2197

a ,b , *c =(2,4,6,8,13)  # c nin degerleri toplamı nedir
print(c[0]+c[1]+c[2]) #27

#KARŞILAŞTIRMA OPERATÖRLERİ UYGULAMA 
 #1 Girilen 2 sayıdan hangisi  büyüktür
sayi1 = int(input("sayi1  ")) #10
sayi2 = int(input("sayi2  ")) #5
sonuc=(sayi1>sayi2)
print(f"{sayi1} {sayi2} den buyuktur {sonuc}") #10 5 den buyuktur True

 #2 Girilen bir sayının  tek çift konrolünü yapınız
sayi= int(input("sayi "))
sonuc = (sayi % 2 == 0)
print(f"sayi cift {sonuc}")  # sayi cift True

 #3 Bir ögrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz 50> basarılı
not1= int(input("not1 "))
not2= int(input("not2 "))
not3= int(input("not3 "))

ortalama = (not1+not2+not3) /3
print(f"ogrencinin not ortalamasi: {round(ortalama,2)} başarı durumu {ortalama>=50}")

#MANTIKSAL OPERATÖRLER UYGULAMA 
#1 Yaşı 18 den büyük yada veli izni varsa bir işte çalışabilir durumunu kontrol ediniz 
veli_izni= False
yas= 18
sonuc = (veli_izni) or (yas>=18)
print(sonuc)  #True

#2 Ders notu 50-100 arasındaysa geçti değilse kaldı yazdırınız
dersnot= 50
sonuc=(dersnot>=50 and dersnot<=100)
print(f"ders gecme durumu {sonuc}" )

#3 Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol et
ortalama= 75
zayifSayisi= 0 
sonuc= ortalama>=70 and zayifSayisi==0
print(sonuc)

#4 işe girmek için en az ön lisans ya da lisans mezunu olma durumunu kontrol et sigara kullanmama koşulu
egitim= "lisans"
sigara=False
sonuc=(egitim== "lisans" or egitim=="ön lisans" and  not(sigara)) #True
print(sonuc)

# Uygulamaya giriş kontrolünü "username" ya da "email" ve "parola" için yapalım
email= "info@fatih.com"
username="fatih"
parola="12345"

girilen_bilgi= input("email ya da username: ")
girilen_parola= input("parola ")
sonuc=(email ==girilen_bilgi or username == girilen_bilgi) and(parola==girilen_parola)
print(sonuc)