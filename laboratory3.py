sal = float(input("Enter your Monthly Salary = "))
loan = float(input("Enter Loan Request Amount = "))
sec = sal * 10
if sal >= 30000 and loan <= sec:
    print("You are eligible to have a loan!")
    loan_interest = loan * .10
    month = int(input("How many months will you pay your loan? = "))
    monthly_payment = loan / month
    print("Your monthly pay with 10% Interest will be", monthly_payment)
else:
     print("You are not eligible for a loan.")
     if sal < 30000:
        print("Reason: Insufficient salary amount.")
     if loan > sec:
        print("Reason: The requested loan amount is too high.")