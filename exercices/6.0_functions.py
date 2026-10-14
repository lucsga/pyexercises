"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.
"""

# 1. In: the function receives a list of monthly budgets in euros.
#
# 2. Process: it adds up the budgets (sum) and divides by the number of months (len). If the list is empty, it does NOT divide (that would be a division by zero).
#
# 3. Out: the function RETURNS the average budget per month, or None if the list is empty (None means "no result").
#
# 4. My function name, and why return rather than print:
#    Name: average_monthly_budget. Reading only the name, you know what you get back, without opening the code.
#
#    Why RETURN and not PRINT:
#    - print only SHOWS the result on the screen, then it is gone: the rest
#      of the program cannot use it (the function gives back None).
#    - return GIVES the result back to the program: it can be stored in a
#      variable, displayed, compared, or used in another calculation.



def average_monthly_budget(budgets):
    """Return the average budget per month, or None if the list is empty."""
    if len(budgets) == 0:
        return None
    return sum(budgets) / len(budgets)


# Same list as exercise 4.0: monthly budgets in euros, January -> August
monthly_budgets = [4200, 3800, 5100, 4600, 6900, 3500, 2800, 5400]

# Three different inputs (a slice [start:end] stops just BEFORE end)
first_quarter = monthly_budgets[0:3]   # January, February, March
summer = monthly_budgets[5:8]          # June, July, August

# Three calls: each result is stored in a variable
all_months_average = average_monthly_budget(monthly_budgets)
first_quarter_average = average_monthly_budget(first_quarter)
summer_average = average_monthly_budget(summer)

print(f"Average, January to August: {all_months_average:.2f} EUR")
print(f"Average, first quarter:     {first_quarter_average:.2f} EUR")
print(f"Average, summer:            {summer_average:.2f} EUR")

# Possible ONLY because the function returns its results
gap = first_quarter_average - summer_average
print(f"The first quarter cost {gap:.2f} EUR more per month than the summer.")

# Check: empty list
empty_result = average_monthly_budget([])
if empty_result is None:
    print("Empty list: no month, so no average.")