import datetime
def calculate_loan_schedule(loan_amount, annual_interest_rate, loan_term_years, start_date):
    monthly_interest_rate = annual_interest_rate / (12 * 100)
    total_months = loan_term_years * 12
    monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -total_months)
    
    remaining_balance = loan_amount
    total_paid = 0
    total_interest_paid = 0
    loan_schedule = []
    
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    
    for month in range(1, total_months + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        total_paid += monthly_payment
        total_interest_paid += interest_payment
        
        current_date = start_date + datetime.timedelta(days=(30 * month))
        
        loan_schedule.append({
            'Month': month,
            'Date': current_date.strftime("%Y-%m-%d"),
            'Monthly Payment': monthly_payment,
            'Principal Payment': principal_payment,
            'Interest Payment': interest_payment,
            'Remaining Balance': remaining_balance
        })
    
    return loan_schedule, total_paid, total_interest_paid


def calculate_real_rate(total_interest_paid, loan_amount):
    real_rate = (total_interest_paid / loan_amount) * 100
    return real_rate


if __name__ == "__main__":
    print("Loan Repayment Schedule Calculator\n")
    
    # Get loan parameters from user
    loan_amount = float(input("Enter the loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (%): "))
    loan_term_years = int(input("Enter the loan term in years: "))
    start_date = input("Enter the start date (YYYY-MM-DD): ")

    loan_schedule, total_paid, total_interest_paid = calculate_loan_schedule(loan_amount, annual_interest_rate, loan_term_years, start_date)

    print("\nLoan Repayment Schedule:")
    print("{:<10} {:<12} {:<15} {:<20} {:<20} {:<20}".format('Month', 'Date', 'Monthly Payment', 'Principal Payment', 'Interest Payment', 'Remaining Balance'))
    for entry in loan_schedule:
        print("{:<10} {:<12} {:<15.2f} {:<20.2f} {:<20.2f} {:<20.2f}".format(entry['Month'], entry['Date'], entry['Monthly Payment'], entry['Principal Payment'], entry['Interest Payment'], entry['Remaining Balance']))
    
    print("\nTotal Paid: ${:.2f}".format(total_paid))
    print("Total Interest Paid: ${:.2f}".format(total_interest_paid))
    
    real_rate = calculate_real_rate(total_interest_paid, loan_amount)
    print("Real Interest Rate: {:.2f}%".format(real_rate))
