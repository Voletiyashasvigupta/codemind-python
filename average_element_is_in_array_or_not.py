n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s=s+i
a=s//n
if(a in l):
    print(True)
else:
    print(False)