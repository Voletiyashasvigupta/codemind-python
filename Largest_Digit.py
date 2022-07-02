n=int(input())
l=0
while(n>0):
    i=n%10
    n=n//10
    if(i>l):
        l=i
print(l)