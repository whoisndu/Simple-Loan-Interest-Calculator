def calculate_loan_schedule(loan_amount, annual_interest_rate, loan_term_years):
    monthly_interest_rate = annual_interest_rate / (12 * 100)
    total_months = loan_term_years * 12
    monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -total_months)
    
    remaining_balance = loan_amount
    total_paid = 0
    total_interest_paid = 0
    loan_schedule = []
    
    for month in range(1, total_months + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        total_paid += monthly_payment
        total_interest_paid += interest_payment
        
        loan_schedule.append({
            'Month': month,
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
    # Example usage:
    loan_amount = 25000000  # Replace this with the actual loan amount
    annual_interest_rate = 21.0  # Replace this with the actual annual interest rate
    loan_term_years = 10  # Replace this with the actual loan term in years

    loan_schedule, total_paid, total_interest_paid = calculate_loan_schedule(loan_amount, annual_interest_rate, loan_term_years)

    print("Loan Repayment Schedule:")
    print("{:<10} {:<15} {:<20} {:<20} {:<20}".format('Month', 'Monthly Payment', 'Principal Payment', 'Interest Payment', 'Remaining Balance'))
    for entry in loan_schedule:
        print("{:<10} {:<15.2f} {:<20.2f} {:<20.2f} {:<20.2f}".format(entry['Month'], entry['Monthly Payment'], entry['Principal Payment'], entry['Interest Payment'], entry['Remaining Balance']))
    
    print("\nTotal Paid: ${:.2f}".format(total_paid))
    print("Total Interest Paid: ${:.2f}".format(total_interest_paid))
    
    real_rate = calculate_real_rate(total_interest_paid, loan_amount)
    print("Real Interest Rate: {:.2f}%".format(real_rate))

