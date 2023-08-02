n=int(input())
lst=map(int,input().split())
sum=0
for i in lst:
    sum=sum+i
if sum%2==0:
    print("1")
else:
    print("0")