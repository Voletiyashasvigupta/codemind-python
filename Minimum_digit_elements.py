n=int(input())
a=list(map(int,input().split()))
k=min(a)
c=d=0
while(k>0):
    r=k%10
    c+=1
    k=k//10
for i in a:
    e=0
    while(i>0):
        x=i%10
        i=i//10
        e+=1
    if(e==c):
        d+=1
print(d)