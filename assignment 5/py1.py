#QUESTION 1
line = str(input('Enter string here: '))

a=0
reverse = ''

for i in line:
     reverse = i + reverse
print(reverse)
