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
Enter the loan amount: 100000
Enter the annual interest rate (%): 5.0
Enter the loan term in years: 3
Enter the start date (YYYY-MM-DD): 2023-07-01
```

6. View the Results: The script will display the loan repayment schedule, including the month, date, monthly payment, principal payment, interest payment, and remaining balance for each month. It will also show the total amount paid, the total interest paid, and the real interest rate.
   
```
Loan Repayment Schedule:
Month      Date          Monthly Payment Principal Payment    Interest Payment     Remaining Balance   
1          2023-07-01    ...             ...                 ...                  ...
2          2023-08-01    ...             ...                 ...                  ...
...

Total Paid: $...
Total Interest Paid: $...
Real Interest Rate: ...%
 ```
**Input Format**
1. Loan Amount: Enter the loan amount as a numerical value without commas or currency symbols.
2. Annual Interest Rate: Enter the annual interest rate as a numerical value. For example, if the interest rate is 5.5%, enter "5.5".
3. Loan Term in Years: Enter the loan term in years as a whole number.
4. Start Date: Enter the start date of the loan in the format "YYYY-MM-DD".

**Assumptions**
1. The loan amount, annual interest rate, loan term, and start date are provided by the user.
2. The interest rate is compounded monthly.
3. The monthly payment remains constant throughout the loan term.
4. The loan repayment schedule assumes equal monthly payments.
5. The script does not account for additional factors such as fees, compounding interest, or variations in monthly payments.
