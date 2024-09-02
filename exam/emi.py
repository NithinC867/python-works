loan_amount=int(input("enter your loan amount "))
intrest_rate=int(input("enter the intrest rate "))
tenure_year=int(input("enter tenure in year "))

p=loan_amount
n=tenure_year*12
r=(intrest_rate/12)/100


emi=p*r*(1+r)**n//((1+r)**n-1)
total_payment=emi*n
total_intrest=total_payment-loan_amount

print(f"your monthly emi is {emi} , total payment {total_payment} and the total intrest you are paying {total_intrest}")
