n=int(input())
a=list(map(int,input().split()))
se=so=0
for i in range(n):
    if(i%2==0):
        se=se+a[i]
    else:
        so=so+a[i]
print(se-so)