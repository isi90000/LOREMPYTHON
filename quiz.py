true = 0
false= 0
print("SUAL1- Azerbaycanin paytaxti haradir?")
print("1. Gence \n 2. London \n 3. Paris \n 4. Baki ")
quiz1 = int(input("Dogru variant secin(1,2,3,4):"))
if quiz1==1:
  print("Sehv Cavab daxil etdiniz")
  false +=2
elif quiz1==2:
  print("Sehv Cavab daxil etdiniz")
  false +=1
elif quiz1==3:
  print("Sehv Cavab daxil etdiniz")
  false +=1  
elif quiz1==4:
  print("Duz Cavab daxil etdiniz")
  true +=1 


print("SUAL2 - Komputerin nece generationsu movcuddur?")
print("1. 4 \n 2. 5 \n 3. 6 \n  4. 7")
quiz2 = int(input("Varianti daxil edin(1,2,3,4):"))
if quiz2==1:
  print("Sehv Cavab daxil etdiniz")
  false +=1
elif quiz2==2:
  print("Duz Cavab daxil etdiniz")
  true +=1
elif quiz2==3:
  print("Sehv Cavab daxil etdiniz")
  false +=1  
elif quiz2==4:
  print("Duz Cavab daxil etdiniz")
  false +=1  
print("Duzgun cavablar sayi:", true, "\n  Sehv cavablar sayi:", false)
