"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.
"""

# 1. In: the list from exercise 4.0: 8 monthly advertising budgets in euros, January to August.
#
# 2. Process, function by function (one sentence each, no "and"):
#    1. total_budget(budgets)        returns the sum of all the budgets.
#    2. highest_budget(budgets)      returns the highest budget.
#    3. share_in_percent(part, total) returns what "part" is, as a % of "total".
#    4. share_of_most_expensive_month(budgets) uses the three above, in this
#       order: total, then highest, then the percentage.
#
# 3. Out: the fourth function RETURNS the share of the most expensive month, in %, or None if the list is empty.
#
# 4. The question my fourth function answers:
#    "What share of the total spending did the most expensive month represent?"
#    If one month weighs very heavily, it must be justified, or the budget should be spread out better.
#
#    Why splitting into three makes it easier to check: each small function
#    does ONE calculation, so I can test it with simple numbers I can check
#    in my head. If the final result is wrong, I test the three pieces one by
#    one and find WHICH one is wrong, instead of searching everywhere at once.
#


def total_budget(budgets):
    """Return the sum of all the budgets."""
    return sum(budgets)


def highest_budget(budgets):
    """Return the highest budget."""
    return max(budgets)


def share_in_percent(part, total):
    """Return what part represents, as a percentage of total."""
    return part / total * 100


def share_of_most_expensive_month(budgets):
    """Return the share of the most expensive month in %, or None if the list is empty."""
    if len(budgets) == 0:
        return None
    total = total_budget(budgets)
    highest = highest_budget(budgets)
    return share_in_percent(highest, total)


# Test each small function on its own first
print("Test total_budget:     ", total_budget([100, 200, 300]), "(expected 600)")
print("Test highest_budget:   ", highest_budget([100, 200, 300]), "(expected 300)")
print("Test share_in_percent: ", share_in_percent(300, 600), "(expected 50.0)")

# Then use them together on the real data
# Same list as exercise 4.0: monthly budgets in euros, January -> August
monthly_budgets = [4200, 3800, 5100, 4600, 6900, 3500, 2800, 5400]

share = share_of_most_expensive_month(monthly_budgets)
print(f"\nThe most expensive month represents {share:.1f}% of the total spending.")

# Empty list: no crash, the function returns None
if share_of_most_expensive_month([]) is None:
    print("Empty list: no month, so no answer.")