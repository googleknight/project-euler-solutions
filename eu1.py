def sum_mul(num):
    ans=0
    x=1
    while x*3<num:
     ans+=x*3
     x+=1
    x=1
    while x*5<num:
     if((x*5)%3!=0):
      ans+=x*5
     x+=1
    return ans
print(sum_mul(1000))
    