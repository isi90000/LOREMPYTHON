print("İş kategoriyası seçin \n 1.Dövlət və neft sektou \n 2.Qeyri-dövlət və qeyri-neft sektoru")
sector = int(input("Sektoru secin 1 ve ya 2 yazin:"))
salary= int(input("Maasini daxil ele:"))
def hesabla(sector,salary):
  if sector==1:
    if salary <=2500:
      revenue_tax=(salary-200)*14/100
    if salary > 2500:
      revenue_tax = 350 + (salary-2500)*25/100
    dsmf=salary*3/100
    issizlik = salary*0.5/100
    if salary<=8000:
      icbari = salary*2/100
    if salary>8000:
      icbari= (salary-8000)*0.5/100 + 160
    net_revenue = salary - icbari - issizlik - dsmf - revenue_tax
    print("Net qazanc:",net_revenue)
    print("Gelir vergisi:",revenue_tax)
    print("DSMF:",dsmf)
    print("Icbari sigorta:",icbari)
    print("issizlik sigorta:",issizlik)
  if(sector==2):
    if salary<=8000:
      revenue_tax=0
      icbari=salary*2/100
    if salary > 8000:
      revenue_tax = (salary-8000)*14/100
      icbari = 160 + (salary-8000)*0.5/100
    if salary<=200:
      dsmf=salary*3/100
    if salary > 200:
      dsmf=(salary-200)*10/100 + 6
      issizlik= salary *0.5/100 
      net_revenue = salary - icbari - issizlik - dsmf - revenue_tax   
      print("Net qazanc:",net_revenue)
      print("Gelir vergisi:",revenue_tax)
      print("DSMF:",dsmf)
      print("Icbari sigorta:",icbari)
      print("issizlik sigorta:",issizlik)
hesabla(sector,salary)  
