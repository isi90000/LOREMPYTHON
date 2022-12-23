import time
gerisayim = int(input("Geri sayim ucun eded daxil edin:"))
while(gerisayim>=0):
  print(gerisayim)
  gerisayim -= 1
  time.sleep(1)
else:
  print("Geri sayim bitti")
