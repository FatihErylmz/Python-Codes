#Dictionary Methodları 
yemekTarifi={
    "yemek_adi": "Makarna",
    "tarif": "tarif aciklamasi",
    "resim" : "1.jpeg"
}
#elemanlara erişim
sonuc=yemekTarifi["yemek_adi"]
print(sonuc) #Makarna

sonuc=yemekTarifi.get("yemek_adi")
print(sonuc) #Makarna


sonuc=yemekTarifi.keys()
print(sonuc) #dict_keys(['yemek_adi', 'tarif', 'resim'])

sonuc=yemekTarifi.values()
print(sonuc) #dict_values(['Makarna', 'tarif aciklamasi', '1.jpeg'])

sonuc=yemekTarifi.items()
print(sonuc) #dict_items([('yemek_adi', 'Makarna'), ('tarif', 'tarif aciklamasi'), ('resim', '1.jpeg')])

#güncelleme ve ekleme
# yemekTarifi["yemek_adi"]="Pilav" # method kullanmadan güncelleme
yemekTarifi.update({"yemek_adi " : "Pilav"}) 
# yemekTarifi["yemek_adi2"]="Pilav" # method kullanmadan ekleme
yemekTarifi.update({"yemek_adi2 " : "Pilav"}) 

sonuc=yemekTarifi
print(sonuc)

# eleman silme
yemekTarifi.pop("yemek_adi")
yemekTarifi.popitem()
#yemekTarifi.clear()

sonuc=yemekTarifi
print(sonuc)