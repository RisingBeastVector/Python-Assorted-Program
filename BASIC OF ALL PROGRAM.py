#BASIC INPUT FORMAT
a = int(input('ENTER A NUMBER: '))
b = int(input('ENTER THE VALUE OF b: '))

#BASIC OUTPUT FORMAT
print()
print("============================='OUTPUT'===============================")
print('SUM OF THE SERIES IS: ')

#BASIC LOGIC FOR SERIES
n = int(input('ENTER THE VALUE OF n: '))
sum = 0
for i in range(1,n+1) :
    sum = sum+i

#BASIC NUMBER PROGRAM LOGIC
t = n
sum = 0
while t!=0 :
    d = t%10
    sum = sum+d
    t = t//10
