#PYTHON PRORAM TO ACCEPT A YEAR AND
#TO CHECK WHETHER IT IS A LEAP YEAR OR NOT.

year = int(input('ENTER YEAR WHICH HAS TO BE CHECKED: '))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print(year, 'IS A LEAP YEAR')

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print(year, 'IS A LEAP YEAR')

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print(year, 'IS NOT A LEAP YEAR')