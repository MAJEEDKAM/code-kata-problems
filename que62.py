a=input()
n=0
for i in range(0,len(a)):
    if(a[i]!='0')and(a[i]!='1'):
        n+=1
if(n>0):
    print("no")
else:
    print("yes")
