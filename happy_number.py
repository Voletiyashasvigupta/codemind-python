n=int(input())
sum=0
while(n>0):
    i=n%10
    n=n//10
    sum=sum+i*i
while(sum>0):
    j=sum%10
    sum=sum//10
    if(j==1 or j==7):
        print(True)
        break
else:
    print(False)