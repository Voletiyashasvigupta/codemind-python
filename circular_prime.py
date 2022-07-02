n=int(input())
temp=n
sum=0
c=0
a=0
for i in range(2,int(n**0.5)+1):         
    if n%i==0:
        c=0
        break
else:
    c+=1
while(temp):
    j=temp%10
    sum=sum*10+j
    temp=temp//10
for i in range(2,int(sum**0.5)+1):         
    if sum%i==0:
        a=0
        break
else:
    a+=1
if(a==c and a!=0 and c!=0):
    print("circular prime")
elif(a==0 and c==1):

    print("prime but not a circular prime")
else:
    print("not prime")