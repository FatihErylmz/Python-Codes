# VALUE VE REFERANS TİPLER

#value types --> deger olarak saklanır

a=10
b=20
a=b
print(a,b) #20 20

a=10
b=20
a=b
b=30
print(a,b) #20 30 

# reference tipler bellekte adres olarak saklanır
a=["elma", "armut"]
b=["elma", "armut"]
a = b # b nin adresini a ya eşitlemiş oluyoruz #adres kopyaladık

a[0]="üzüm"
print(a,b) #['üzüm', 'armut'] ['üzüm', 'armut']


#liste kopyalama
listeA=[10,20]
ListeB=listeA.copy()  #KOPYALAMA 1.YÖNTEM
ListeB=list(listeA) # KOPYALAMA 2.YÖNTEM
ListeB[0]= 30
print(listeA,ListeB) #[10, 20] [30, 20]