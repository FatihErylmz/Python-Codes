#LİSTE METHODLARI UYGULAMA 

customers=["Fatih","Hüseyin" ,"Ertuğrul","Çağlar"]
order_totals=[12000,13000,5000,15000]

#1 Çağla kullancı adıyla yapılan 3000 liralık siparişi ekleyin
customers.append("Çağla")
order_totals.append(5000)
sonuc=customers , order_totals

print(sonuc)

#2 Son eklenen siparişi siliniz
customers.pop()
order_totals.pop()

#3 Herhangi bir müşteri için  özet cümleyi yazdırın 

# '<username>' isimli müşterinin sipariş toplamı <> liradır 
yazdir= f"{customers[0]} isimli müşterinin sipariş toplami {order_totals[0]} liradir"
print(yazdir) #Fatih  isimli müşterinin sipariş toplami 12000 liradır

#4 musterileri alfabetik olarak sıralayınız
customers.sort()
print(customers) #['Ertuğrul', 'Fatih ', 'Hüseyin', 'Çağlar']

#5 Siparis  toplamlarını azalan şekilde sıralayınız 
order_totals.sort() # once sırala
order_totals.reverse()
print(order_totals) #[15000, 13000, 12000, 5000]

#6 En dusuk siparis hangisidir
sonuc=min(order_totals)
print(sonuc) #5000

#7 Fatih kullanıcısının kac siparisi vardir 

kac = customers.count('Fatih')
print(kac) #1 count --> tekrar sayisini döndürür

#8 customers listesindeki Ertuğrul kullanıcısını siliniz
print(customers.remove("Ertuğrul"))
print(customers) #['Fatih', 'Hüseyin', 'Çağlar']

#9 Listedeki tüm içerikleri siliniz
customers.clear()
order_totals.clear()

#10 Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlaeını listeye ekleyiniz
username= input("Musteri Adi ")
totalmarkt = input("Toplam ")
customers.append(username)
order_totals.append(totalmarkt)
print(customers)
print(order_totals)