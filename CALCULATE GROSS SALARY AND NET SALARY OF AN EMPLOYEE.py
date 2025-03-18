#PYTHON PROGRAM TO CALCULATE GROSS SALARY AND NET SALARY OF AN EMPLOYEE BY ACCEPTING HIS NAME, PHONE NUMBER, BASIC SALARY AND BY USING THE BELOW DATA :
#DA = 25% of BASIC
#HRA = 15% of BASIC,
#PF = 12% of BASIC.
#NET PAY = Basic + DA + HRA
#GROSS PAY = NET PAY - PF.

   
name = input("ENTER NAME OF THE EMPLOYEE :")
ph = int(input("ENTER PHONE NUMBER OF EMPLOYEE : "))
basic = float(input("ENTER BASIC SALARY OF EMPLOYEE :"))
da=basic*0.2
hra=basic*0.15
pf=(basic+da)*0.12
netpay=basic+da+hra
grosspay=netpay-pf
print("\n\n")
print("S A L A R Y D E T A I L E D B R E A K U P ")
print("=========================================")
print(" NAME OF EMPLOYEE : ",name)
print(" PHONE NUMBER OF EMPLOYEE : ",ph)
print(" BASIC SALARY : ",basic)
print("=========================================")
print(" DEARNESS ALLOWANCE : ",da)
print(" HOUSE RENT ALLOWANCE : ",hra)
print(" NET SALARY PAY : ",netpay)
print(" PROVIDENT FUND : ",pf)
print(" GROSS PAYMENT : ",grosspay)