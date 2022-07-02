n=int(input())
temp=n
p=n*n
c=0
r=0
sum=0
while(n):
    i=n%10
    c+=1
    n=n//10
for j in range(c):
    k=p%10
    sum=sum*10+k
    p=p//10
while(sum):
    a=sum%10
    r=r*10+a
    sum=sum//10
if(temp==r):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")