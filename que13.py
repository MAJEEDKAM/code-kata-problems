num=int(input())

n=0

for i in range(2,num-1):
    if (num%i==0):
        n=1

if n==0:
    print("yes")
else:
    print("no")
