n=int(input())
temp=n
sum=0
while(n>0):
    i=n%10
    n=n//10
    sum=sum*10+i
if(sum==temp):
    print(True)
else:
    print(False)