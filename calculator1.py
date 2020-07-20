import math
print("Enter the credit principal:")
credit = int(input())
print('''What do you want to calculate? 
type "m" - for count of months, 
type "p" - for monthly payment:''')
calc = input()
if(calc == "m"):
    print("Enter monthly payment:")
    monthly = int(input())
    no = math.ceil(credit/monthly)
    if(no > 1):
        print("It takes " + str(no) + " months to repay the credit")
    else:
        print("It takes " + str(no) + " month to repay the credit")
elif(calc == "p"):
    print("Enter count of months:")
    monthly = int(input())
    no = math.ceil(credit/monthly)
    if(credit % monthly == 0):
        print("Your monthly payment = " + str(no))
    else:
        lastpayment = credit - (monthly - 1)*no
        print("Your monthly payment = " +  str(no) + " with last month payment = " + str(lastpayment) + ".")
