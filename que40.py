num=int(input())
first=0
sec=1
print(sec,end=" ")
for i in range(2,num+1):
    next1=first+sec
    print(next1,end=" ")
    first=sec
    sec=next1
