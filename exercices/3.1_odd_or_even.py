"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.
"""

# 1. In: a whole number N typed by the user. 
#
# 2. Process: check that N is acceptable, then for each number i from 1 to N,compute i % 2 (the remainder of the division by 2).
#
# 3. Out: one line per number, with "odd" or "even".
#
# 4. What happens on 0, on a negative number, on a very large number:
#    Decision for all three: refuse the value, explain why, and ask again.
#    - 0: "from 1 to 0" contains no numbers. The program would print nothing,
#      which looks like a bug. Better to tell the user and ask again.
#    - Negative (e.g. -4): we count UP from 1, so "from 1 to -4" makes no
#      sense. Ask again.
#    - Very large (e.g. 5000): 5000 lines scrolling by is useless, nobody can
#      read them. I set a limit MAX_N = 100 (easy to change) and ask again.

MAX_N = 100


def ask_n():
    """Ask until the user types a whole number between 1 and MAX_N."""
    while True:
        text = input(f"Enter a whole number between 1 and {MAX_N}: ")
        try:
            n = int(text)
        except ValueError:
            print(f"'{text}' is not a whole number, please try again.")
            continue
        if n == 0:
            print("0 gives an empty list (there is nothing from 1 to 0). Please try again.")
        elif n < 0:
            print("A negative number makes no sense here: we count up from 1. Please try again.")
        elif n > MAX_N:
            print(f"{n} is too large: that would print {n} lines. The limit is {MAX_N}. Please try again.")
        else:
            return n


n = ask_n()

for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")