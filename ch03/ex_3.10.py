"""
3.10 (Hourly Wage Calculator) Reimplement Exercise 2.12 to use a loop that calculates
and displays the hourly wage an employee earns after a good performance review for years
1 through 10.
    2.12 (Hourly Wage Calculator) Every year, if an employee receives a good job performance
    review, they get a raise of 3% on their wages. In turn, if they receive a suboptimal performance
    review, their wages are deducted by 3%. Consider an employee starting with an hourly wage
    of $10. Calculate how much this employee is earning after 5 years of consistent good reviews
    and after 2 years of bad reviews. Use the following formula to calculate these wages:
    w = o(1 + p)^n
    where
    w is the new hourly wage,
    o is the original hourly wage,
    p is the percentage increase or decrease, and
    n is the number of years with an increase or decrease in hourly wage.
"""
w = 10
for year in range(1,11):
    nw = w * (1 + .03)**year
    print(f'Año: {year:>2} - {nw:>5.3f}')
    w = nw
