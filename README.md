# simple-loan-interest-calculator
**Loan Repayment Schedule Calculator**
This Python script calculates a loan repayment schedule based on the provided loan amount, annual interest rate, and loan term in years. It also calculates the total amount paid, the total interest paid, and the real interest rate.

**Usage**
1. Install Python: Make sure you have Python installed on your system. You can download it from the official Python website: python.org.
2. Clone the Repository: Clone this repository to your local machine or download the code as a ZIP file.
3. Run the Script: Open a terminal or command prompt and navigate to the directory where the script is located. Execute the following command:
```python loan_repayment_schedule.py```
4. Modify Loan Parameters: Inside the script, you can modify the loan parameters to calculate the loan repayment schedule for different scenarios. Replace the placeholders with the actual loan amount, annual interest rate, and loan term in years.
   
```
loan_amount = 100000  # Replace this with the actual loan amount
annual_interest_rate = 5.0  # Replace this with the actual annual interest rate
loan_term_years = 3  # Replace this with the actual loan term in years
```

6. View the Results: The script will display the loan repayment schedule, including the monthly payment, principal payment, interest payment, and remaining balance for each month. It will also show the total amount paid, the total interest paid, and the real interest rate.

```
Loan Repayment Schedule:
Month      Monthly Payment Principal Payment    Interest Payment     Remaining Balance
1          ...             ...                 ...                  ...
2          ...             ...                 ...                  ...
Total Paid: $...
Total Interest Paid: $...
Real Interest Rate: ...%
 ```
**Assumptions**
1. The loan amount, annual interest rate, and loan term are provided as input.
2. The interest rate is compounded monthly.
3.The monthly payment remains constant throughout the loan term.
4. The loan repayment schedule assumes equal monthly payments.
5. The script does not account for additional factors such as fees, compounding interest, or variations in monthly payments.
