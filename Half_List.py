n=int(input())
arr=list(map(int,input().split()))
k=n//2
for i in range(n-1,k-1,-1):
    print(arr[i],end=" ")
for i in range(k):
    print(arr[i],end=" ")