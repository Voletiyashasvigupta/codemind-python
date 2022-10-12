n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i<0:
        i=i*(-1)
    if i==0:
        b.append(1)
        continue
    c=0    
    while i:
        i=i//10
        c+=1
    b.append(c)
k=max(b)
for i in range(n):
    if b[i]==k:
        print(a[i],end=' ')