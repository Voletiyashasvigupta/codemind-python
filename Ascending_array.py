n=int(input())
a=list(map(int,input().split()))
k=set(a)
x=sorted(k)
if(x==a):
    print("yes")
else:
    print("no")
    