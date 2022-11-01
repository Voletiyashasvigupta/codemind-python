n=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
for i in l:
    if(i==0):
        l.append(i)
        continue
    elif(l.count(i)==i):
        c=c+1
        l1.append(i)
if(c==0):
    print(-1)
else:
    print(min(l1),max(l1))