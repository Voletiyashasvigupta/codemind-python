n=input()
v='aeiouAEIOU'
c=0
b=[]
for i in n:
    if(i in v):
        c+=1
        if i not in b:
            b.append(i)
print(*b)
if(c==0):
    print("-1")