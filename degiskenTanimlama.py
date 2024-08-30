#Değişken Tanımlama Uygulaması

"""
Aşağida müşterinin bilgilerini ve satin aldigi ürün bilgilerini değişkenler içerisinde saklayiniz

Toplam ödenen ücret nedir ?

Ödenen miktarin kdv orani nedir %18
Fatih Eryılmaz
0532 123 4567
info@fatih.com
Türkiye

Satin alinan ürünler

ürün adi = kablosuz mouse fiyat 550 tl 
ürün adi = kablosuzklavye fiyat 650 tl 
ürün adi = Dizüstü Bilgisayar fiyat 55000 tl 

"""
#müşteri bilgileri
musteri_ad= "Fatih"
musteri_soyad= "Eryılmaz"
musteri_tel = "0532 123 4567"
musteri_mail ="info@fatih.com" 
musteri_konum = "Türkiye"

#satin alinan ürünler 

urun1 = "Kablosuz Mouse"
urun1Fiyat = 550

urun2= "Kablosuz klavye"
urun2Fiyat= 650

urun3= "Dizüstü Bilgisayar"
urun3Fiyat= 55000

toplamSepet = urun1Fiyat+urun2Fiyat+urun3Fiyat
kdv_oranimiz = 0.18
toplamKdv = toplamSepet +(toplamSepet)*kdv_oranimiz

#istenen sonuclar
print("kdvsiz fiyat " +str(toplamSepet))
print("kdvli fiyat " +str(toplamKdv))