def fibo(num):
 first=1
 second=2
 if num<3:
  return num
 else:
  for i in range(2,num):
   sum=first+second
   first=second
   second=sum
   if second>=4000000:
    return first
 return second
sum=0
for i in range (1,33):
 if fibo(i)%2==0:
  sum+=fibo(i)
print(sum)