"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.
"""

# 1. In: the list from exercise 4.0, copied as is: 8 monthly advertising budgets in euros, January to August, plus the month names.
#
# 2. Process: compute the total and the average ONCE, before the loop.
#    Then, for EACH budget, compute:
#    - its share of the total.
#    - whether it is above or below the average.
#
# 3. Out: one line per month: position, month, budget, share of the total, above/below average.
#
# 4. What I compute for each item, and why it is worth showing:
#    The SHARE OF THE TOTAL shows which months weighed most in the spending (May alone is 19% of the total, July only 7.7%).
#    ABOVE/BELOW AVERAGE shows which months need to be justified or watched.


MONTHS = ["January", "February", "March", "April",
          "May", "June", "July", "August"]

# Same list as exercise 4.0: monthly budgets in euros, January -> August
monthly_budgets = [4200, 3800, 5100, 4600, 6900, 3500, 2800, 5400]

# Computed once, before the loop
total = sum(monthly_budgets)
average = total / len(monthly_budgets)

# One line per item
for position, budget in enumerate(monthly_budgets, start=1):
    month = MONTHS[position - 1]
    share = budget / total * 100

    if budget > average:
        status = "above average"
    else:
        status = "below average"

    print(f"{position}. {month}: {budget} EUR = {share:.1f}% of the total, {status}")