def calculate_debt_payoff(balance, interest_rate, monthly_payment):
    """ Calculate how long it will take to pay off the debt """
    interest_rate = interest_rate / 100 / 12  # Monthly interest rate
    months = 0
    while balance > 0:
        balance = balance + balance * interest_rate - monthly_payment
        months += 1
        if balance < 0:
            break
    return months

def main():
    print("Welcome to Debt Tracker!")
    balance = float(input("Enter the total debt balance: $"))
    interest_rate = float(input("Enter the interest rate (annual %): "))
    monthly_payment = float(input("Enter the monthly payment: $"))

    months = calculate_debt_payoff(balance, interest_rate, monthly_payment)
    years = months // 12
    remaining_months = months % 12

    print(f"\nIt will take {years} years and {remaining_months} months to pay off your debt.")
    print(f"Total paid over this period: ${monthly_payment * months}")

if __name__ == "__main__":
    main()
