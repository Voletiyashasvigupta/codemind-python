n=int(input())
s=0
while(n>=10):
    s=0
    r=0
    while(n>0):
        r=n%10
        s=s+r
        n=n//10
    if(s>=10):
        n=s
        continue
    else:
        print(s)
        break

