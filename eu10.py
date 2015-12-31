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

sum=0            
for x in range(2000001):
 if is_prime(x):
   sum+=x
print (sum)