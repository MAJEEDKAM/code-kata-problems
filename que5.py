a=input()
b=input()
c=input()

if (a > b) and (a > c):
   large = a
elif (a < b) and (b > c):
   large = b
else:
   large = c

print(large)

