#PYTHON PROGRAM TO INPUT A NUMBER AND PRINT ALL THE ODD NUMBERS FROM 0 TO TILL THAT NUMBER
#AND FIND ITS SUM.

num = int(input('ENTER A NUMBER: '))
sum=0
for i in range(num) :
    if i%2!=0 :
        sum=sum+i
print("SUM OF ALL ODD NUMBERS TILL",num,"IS : ",sum)
