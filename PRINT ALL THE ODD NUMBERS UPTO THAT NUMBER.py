#PYTHON PROGRAM TO INPUT A NUMBER AND PRINT ALL THE ODD NUMBERS UPTO THAT NUMBER.

a = int(input('ENTER A NUMBER: '))
for i in range(a) :
    if i%2!=0 :
        print(i, end=' ; ')