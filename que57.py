x, z = input().split()
y=list(map(str,input().split()))
count=0;
for i in range(0,len(y)):
    if(y[i]==z):
        count+=1
print(count)
