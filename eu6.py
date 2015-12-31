def sumsq(num):
 s=0
 for i in range(1,num+1):
  s+=i**2
 return s
def sqsum(num):
 s=0
 for i in range(1,num+1):
  s+=i
 s=s**2
 return s
print (abs(sumsq(100)-sqsum(100)))