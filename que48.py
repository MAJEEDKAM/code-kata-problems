length=int(input())
sum=0
x=list(map(int,input().split()))
for i in x:
    sum+=i
print(sum//length)
