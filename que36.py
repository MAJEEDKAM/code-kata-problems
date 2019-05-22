import re
paragraph=input()
count=0
for i in paragraph:
    if re.match("^[.,@_!#$%^&*()<>?/\|}{~:]*$",i):
                   count+=1
print(count)
