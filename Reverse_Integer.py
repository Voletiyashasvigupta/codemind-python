def rev(a):
    r=0
    while a>0:
        rem=a%10
        r=(r*10)+rem
        a//=10
    return r
a=int(input())
f=0
if a<0:
    f=1
    a*=-1
ar=rev(a)
if f==1:
    print(ar*-1)
else:
    print(ar)