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
for x in range(2,int(sqrt(600851475143))):
 if is_prime(x):
  if 600851475143%x==0:
   print (x)