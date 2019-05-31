x=input()
m,n=0,0
for i in x:
    if i.isnumeric() and m==0:
        m=1
    if i.isalpha() and n==0:
        n=1
if m==1 and n==1:
    print("Yes")
else:
    print("No")
