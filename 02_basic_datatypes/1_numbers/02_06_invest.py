'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
investment_amount=input("investment amount: ")
interest_rate=input("interest rate: ")
years=input("number of years: ")
print(float(investment_amount)*float(interest_rate)*float(years))
