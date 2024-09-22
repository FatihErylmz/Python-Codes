#IDENTITY - MEMBERSHIP
#identity

x= [2,4,6]
y= [2,4,6]
z=y
print(x==y) #True
print(x is y) #False çünkü x ve y aynı nesne değildir 2 farklı nesneyı temsıl eder 
print(x is not  y) #True
print(z is y)  #True

# membership

print(20 in x) #False
print(20 not in x) #True