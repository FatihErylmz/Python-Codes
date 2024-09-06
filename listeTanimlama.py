#Liste Tanımlama
programlama_diller= ["Python","C","Javascript","C#"]
sonuc = programlama_diller[0:2] #['Python', 'C']  başlangıcta dahil sonda dahil değil 
sonuc = programlama_diller[:2] #['Python', 'C']
sonuc = programlama_diller[0:] #['Python', 'C', 'Javascript', 'C#']
sonuc = programlama_diller[-3:-1] #['C', 'Javascript']
sonuc = programlama_diller[-3:] #['C', 'Javascript', 'C#']

#guncelleme
programlama_diller[-1] = "C++"
sonuc=programlama_diller
# ['Python', 'C', 'Javascript', 'C++']

#eleman sayısının kac oldugu
sonuc=len(programlama_diller) #4

#listeye ekleme  
sonuc= programlama_diller+["Go" , "Delphi"] 
#['Python', 'C', 'Javascript', 'C++', 'Go', 'Delphi']

# Liste üzerinde bir eleman var mı yok mu 
sonuc= "Python" in programlama_diller  # True 
print(sonuc) 

#döngü

for i in programlama_diller:
    print(i)
    """
    Python
    C
    Javascript
    C++
    """
#indeksteki elemanı sılme 
del programlama_diller[2]