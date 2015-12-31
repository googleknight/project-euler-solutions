#find smallest number which is divisible first 20 numbers
from math import sqrt
def is_prime(x):
    i=2
    while i**2<=x:
        if x%i==0:
            return False
        i+=1
    else:
        if x>1:
            return True
        else:
            return False   
def get_fact(num):
 lst=[]
 for x in range(2,int(sqrt(num)+1)):
  if is_prime(x):
   if num%x==0:
    lst.append(x)
 return lst
num=1
for i in range(2,21):
 if is_prime(i):
  num*=i
 elif num%i!=0:
   fact=get_fact(i)
   count=0
   while num%i!=0:
    num*=fact[count]
    count+=1
print(num)