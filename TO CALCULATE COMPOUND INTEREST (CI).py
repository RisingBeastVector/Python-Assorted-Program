# WRITE A PROGRAM TO CALCULATE COMPOUND INTEREST (C.I.).
P = float(input('ENTER PRINCIPAL AMOUNT: '))
R = float(input('ENTER RATE OF INTEREST: '))
T = float(input('ENTER TIME PERIOD: '))
Amount = P*(pow((1+R /100),T))
CI = Amount - P
print('COMPOUND INTEREST (C.I.) IS: ', CI)
 
