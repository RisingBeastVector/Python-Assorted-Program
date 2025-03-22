#WRITE A MENU-DRIVEN PROGRAM TO COMPUTE AREA AND PERIMETER OF DIFFERENT
#2D SHAPES SUCH AS TRIANNGLE OR SQUARE OR PARALLELOGRAM OR RECTANGLE OR
#TRAPEZIUM OR RHOMBUS OR CIRCLE.

print('CHOOSE 1 FOR TRIANGLE')
print('CHOOSE 2 FOR SQUARE')
print('CHOOSE 3 FOR PARALLELOGRAM')
print('CHOOSE 4 FOR RECTANGLE')
print('CHOOSE 5 FOR TRAPEZIUM')
print('CHOOSE 6 FOR RHOMBUS')
print('CHOOSE 7 FOR CIRCLE')

choice = int(input('INPUT YOUR CHOICE: '))

if choice == 1:
    s1 = int(input('ENTER SIDES OF TRAINGLE: '))
    s2 = int(input('ENTER SIDES OF TRAINGLE: '))
    s3 = int(input('ENTER SIDES OF TRAINGLE: '))
    base = int(input('ENTER BASE &  OF TRAINGLE: '))
    height = int(input('ENTER HEIGHT OF TRAINGLE: '))
    area1 = (1/2)*base*height
    peri1 = s1+s2+s3
    print('AREA OF TRIANGLE IS: ', area1, 'PERIMETER OF TRIANGLE IS: ', peri1)

elif choice == 2:
    l = int(input('ENTER A SIDE OF SQUARE: '))
    area2 = l**2
    peri2 = 4*l
    print('AREA OF SQUARE IS: ', area2, 'PERIMETER OF SQUARE IS: ', peri2)
     
elif choice == 3:
    a = int(input('ENTER SIDE OF PARALLELOGRAM: '))
    base = int(input('ENTER BASE OF PARALLELOGRAM: '))
    height = int(input('ENTER HEIGHT OF PARALLELOGRAM: '))
    area3 = base*height
    peri3 = 2*(a+base)
    print('AREA OF PARALLELOGRAM: ', area3, 'PERIMETER OF PARALLELOGRAM IS: ', peri3)

elif choice == 4:
    l1 = int(input('ENTER LENGTH OF RECTANGLR: '))
    b = int(input('ENTER BREADTH OF RECTANGLE: '))
    area4 = l1*b
    peri4 = 2*(l1+b)
    print('AREA OF RECTANLE IS: ', area4, 'PERIMETER OF RECTANGLE IS: ', peri4)

elif choice == 5:
    p1 = int(input('ENTER LENGTH OF PARALLEL SIDES OF TRAPEZIUM: '))
    p2 = int(input('ENTER LENGTH OF PARALLEL SIDES OF TRAPEZIUM: '))
    s3 = int(input('ENTER LENGTH OF NON-PARALLEL SIDES OF TRAPEZIUM: '))
    s4 = int(input('ENTER LENGTH OF NON-PARALLEL SIDES OF TRAPEZIUM: '))
    height2 = int(input('ENTER HEIGHT OF TRAPEZIUM: '))
    area5 = (1/2)*(p1+p2)*height2
    peri5 = p1+p2+s3+s4
    print('AREA OF TRAPEZIUM IS: ', area5, 'PERIMETER OF TRAPEZIUM IS: ', peri5)

elif choice == 6:
    d1 = int(input('ENTER LENGTH OF DIAGONAL OF RHOMBUS: '))
    d2 = int(input('ENTER LENGTH OF DIAGONAL OF RHOMBUS: '))
    side = int(input('ENTER LENGTH OF DIAGONAL OF RHOMBUS: '))
    area6 = (1/2)*d1*d2
    peri6 = 4*side
    print('AREA OF RHOMBUS IS: ', area6, 'PERIMETER OF RHOMBUS IS: ', peri6)

elif choice == 7:
    radius= int(input('ENTER THE RADIUS OF CIRCLE: '))
    pi = 3.14
    area7 = pi*radius*radius
    peri7 = 2*pi*radius
    print('AREA OF CIRCLE IS: ', area7, 'PERIMETER OF CIRCLE IS: ', peri7)

else:
    print('INVALID CHOICE. ENTER FROM THE ABOVE MENTIONED CHOICE')
