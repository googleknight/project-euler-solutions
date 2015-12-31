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
count=0
i=2
while True:
 if is_prime(i):
  count+=1
 if count==10001:
   print(i)
   break
 i+=1