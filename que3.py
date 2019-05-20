char =(input())

vowels=['a','e','i','o','u','A','E','I','O','U']

if char.isdigit():
        print("invalid")

elif char in vowels:
        print("Vowels")

else:
        print("Consonant")
