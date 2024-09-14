#SETS
meyveler={"elma","armut","kiraz","elma"}

sonuc=meyveler
print(sonuc) #{'elma', 'armut', 'kiraz'} #sıralar degisiyor ve tekrarlanmıyor

#elemanlara erişim
for x in meyveler:
    print(x)   
    # elma
    # armut
    # kiraz

# liste içerisinde elmamnın varlığını sorgulayabiliriz
sorgula= "elma" in meyveler
sorgula= meyveler
print(sorgula)  #True

meyveler.add("karpuz")
sonuc=meyveler
print(sonuc) #eklenirken rastgele bir  indekse eklenir


# liste içerisinde elmamnın varlığını sorgulayabiliriz
sorgula= "elma" in meyveler
sorgula=meyveler
print(sorgula)  #True

# meyveler.remove("vişne") # raise an error
# meyveler.discard("armut")
# meyveler.pop() #rastgele siler cünkü set lerde indeksleme yok
# meyveler.clear() #tümünü siler