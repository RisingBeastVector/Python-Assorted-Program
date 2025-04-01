#WRITE A PROGRAM TO CALCULATE BMI.
mass = int(input('ENTER WEIGHT : '))
hcm = int(input('ENTER HEIGHT IN CENTIMETERS : '))
hm = hcm/100 #to convert height in cm to height in meters.
BMI = mass/hm**2
print('BMI IS : ', BMI)
