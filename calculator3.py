import math
print('''What do you want to calculate? 
type "n" - for count of months, 
type "a" - for annuity monthly payment,
type "p" - for credit principal:''')
what = input()
if what == "n":
    print("Enter credit principal:")
    credit = float(input())
    print("Enter monthly payment:")
    monthly = float(input())
    print("Enter credit interest:")
    interest = float(input())
    i = interest/(12*100)
    num = monthly/(monthly - (i*credit))
    n = math.ceil(math.log(num, 1 + i))
    print(str(int(n/12)) + ' years and ' + str(n%12) + ' months to repay this credit!')
elif what == "a":
    print("Enter credit principal:")
    credit = int(input())
    print("Enter count of periods:")
    numOfPayments = int(input())
    print("Enter credit of interest:")
    interest = float(input())
    i = interest/(12*100)
    A = credit*((i*(1+i)**numOfPayments)/((1+i)**numOfPayments - 1))
    print("Your annuity payment = " + str(math.ceil(A)) + "!")
elif what == "p":
    print("Enter monthly payment:")
    A = float(input())
    print("Enter count of periods:")
    n = int(input())
    print("Enter credit interest:")
    interest = float(input())
    i = interest/(12*100)
    P = A/((i*(1+i)**n)/((1+i)**n -1))
    print("Your credit principal = " + str(round(P)) + "!")