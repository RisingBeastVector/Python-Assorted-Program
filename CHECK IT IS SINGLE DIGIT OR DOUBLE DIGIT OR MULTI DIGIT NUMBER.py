#PYTHON PROGRAM TO INPUT A NUMBER AND
#CHECK IT IS SINGLE DIGIT OR DOUBLE DIGIT OR MULTI DIGIT NUMBER.

import math
A = int(input('ENTER A NUMBER: '))
abs=math.fabs(A)        #abs() function can also be used to find absolute value
if abs>=0 and abs<=9 :
    print(A,'IS A SINGLE DIGIT NUMBER')
elif abs>=10 and abs<=99 :
    print(A,'IS A DOUBLE DIGIT NUMBER')
else :
    print(A,'IS A MULTI DIGIT NUMBER')
