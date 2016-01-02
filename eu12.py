from math import sqrt
def count_div(num):
 count=0
 for x in range(1,int(sqrt(num)+1)):
  if num%x==0:
   count+=2
 return count

n=2000
num=(n*(n+1))/2
while True:
 some=count_div(num)
 if some<500:
  print (n,some)
  n+=1
  num=(n*(n+1))/2  
 else:
  print(num,n,some)
  break