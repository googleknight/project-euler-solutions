def pal(num):
 n=str(num)
 rev=n[::-1]
 if n==rev:
  return True
first=999
second=999
gap=1
while True:
 
 if first<=100:
  print(gap)
  gap+=1
 if pal(first*second):
  if second-first<gap:
   print(first*second)
   print(first,second)
   break
  else:
   first=second-1
   second-=1
 first-=1
 
 
