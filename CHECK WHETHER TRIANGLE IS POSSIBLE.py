#PYTHON PROGRAM TO INPUT 3 SIDES OF A TRIANGLE AND
#CHECK WHETHER TRIANGLE IS POSSIBLE OR NOT.

a = int(input('ENTER SIDE OF A TRIANGLE: '))
b = int(input('ENTER SIDE OF A TRIANGLE: '))
c = int(input('ENTER SIDE OF A TRIANGLE: '))
if a+b>c :
    print('TRIANGLE IS POSSIBLE')
elif b+c>a :
    print('TRIANGLE IS POSSIBLE')
elif c+a>b :
    print('TRIANGLE IS POSSIBLE')
else :
    print('TRIANGLE IS NOT POSSIBLE')
