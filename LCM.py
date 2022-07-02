a,b=map(int,input().split())
h=1
c=0
for i in range(1,b+1):
    if(a%i==0 and b%i==0):
        c=1
        if(c==1):
            h=i
l=(a*b)//h
print(l)