#apr -> annual interest rate

def main():
    print("This is a monthly interest payment calculator!")
    print("")
    
    principal = float(input("Enter the principal loan amount: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years: "))
    
    monthly_interest_rate = apr / 1200
    
    months = years * 12
    
    monthly_payment = (principal * monthly_interest_rate)


main()