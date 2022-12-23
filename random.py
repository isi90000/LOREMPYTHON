from time import time_ns
def random(a=128):
  k=time_ns()%a
  return chr(k)
for i in range(12): 
 print(random(),end="")
