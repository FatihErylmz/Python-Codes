#Veri tipleri uygulaması 
"""
Uygulama 1: yarıçapı verilen bir dairenin alanı ve çevresi
alan= πr^2
cevre 2πr
"""
pi=3.14 
yaricap= float(input("Klavyeden yaricap giriniz "))
alan = pi*yaricap*yaricap
cevre = 2*pi*yaricap

print("yaricap " + str(yaricap))
print("alan " +str(alan))
print("cevre " + str(cevre))

"""
Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayın
mil = km/ 1.609344 
"""
km = float(input("km cinsinden değer giriniz "))
mil = float(km/1.609344)
print("Girilen deger " + str(km) + " km " + " mil karsiligi " + str(mil) + " mil")