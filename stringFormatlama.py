# String Formatlama 
name= "Fatih"
surname="Eryilmaz"
ticket= 5
msj= "My name {} {}.  I have  {} ticket".format(name,surname,ticket)
                                                #My name Fatih Eryilmaz.  I have  5 ticket
msj= "My name {0} {1}.  I have  {2} ticket".format(name,surname,ticket)

msj= "My name {a} {s}.  I have  {t} ticket".format(a=name, s=surname, t=ticket)
print(msj)

#f stirng
msj= f"My name {name} {surname}.  I have  {ticket} ticket".format(name, surname, ticket)
print(msj)