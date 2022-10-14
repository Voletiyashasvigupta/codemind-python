n=int(input())
a=list(map(int,input().split()))
k=int(input())
sum=0
for i in a:
    sum+=i
    if(i==k):
        break
print(sum)