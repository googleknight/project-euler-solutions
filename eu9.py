def triplet(num):
 a=1
 b=2
 c=num
 while a**2+b**2<c**2 and b<c :
  while a**2+b**2<c**2 and a<b:
   a+=1
  if a**2+b**2==c**2 and a+b+c==1000:
   return [a,b]
  else:
   a=1
   b+=1
 return [-1,-1]

c=500

while c>100:
 if triplet(c)!=[-1,-1]:
  print(triplet(c))
  print(c)
  break
 c-=1