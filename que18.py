a,b=input().split()
x=int(a)
y=int(b)

for i in range (x,y+1):
        sum = 0
        temp = i
        while (temp>0):
                digit = temp%10
                sum+= digit ** 3
                temp //= 10
                if i == sum:
                        print (i,end=" ")

