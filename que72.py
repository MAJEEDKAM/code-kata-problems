a=input()
count=0
array=['a','e','i','o','u','A','E','I','O','U']
for i in a:
    if i in array:
        count=1
        break
if count==1:
    print("yes")
else:
    print("no")
