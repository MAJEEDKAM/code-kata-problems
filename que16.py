a,b=input().split()
x=int(a)
y=int(b)
  
for i in range(x+1, y): 
   if i > 1: 
       for n in range(2, i): 
           if (i % n) == 0: 
               break
       else: 
           print(i, end=" ") 
