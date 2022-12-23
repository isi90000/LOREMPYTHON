import math
print("Emeliyyati secin: \n 1.toplama \n 2. chixma \n 3. vurma \n 4. bolme \n 5. sinus tap \n 6. cos tap")
choice = int(input("Emeliyyat nomresi secin(1,2,3,4,5,6):"))
def toplama(x,y):
  return x+y
def chixma(x,y):
  return x-y
def vurma(x,y):
  return x*y
def bolme(x,y):
  return x/y
def sinus(x):
  return math.sin(x)
def cosinus(x):
  return math.cos(x)
if choice in(1,2,3,4):
  x= int(input("Birinci reqemi daxil edin:"))
  y= int(input("Ikinci reqemi daxil edin:"))
  if choice==1:
    print(x , "+", y , "=", toplama(x,y))  
  if choice==2:
    print(x , "-", y , "=", chixma(x,y)) 
  if choice==3:
    print(x , "*", y , "=", vurma(x,y))  
  if choice==4:
    print(x , "/", y , "=", bolme(x,y))    
if choice in(5,6):
  x= int(input("reqemi daxil edin:"))
  if choice==5:
    print("CAVAB:", sinus(x)) 
  if choice==6:
    print("CAVAB:", cosinus(x)) 
else:
  print("Duzgun secim edin!")
