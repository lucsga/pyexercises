"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.
"""

# 1. In: two numbers that the user types.
#
# 2. Process: convert each text into a number (float), then compute a + b, a - b, a * b and a / b.
#
# 3. Out: four lines on the screen, one per operation, showing the result.
#
# 4. What happens when the second number is zero, and why:
#    Decision: display a message instead of the division result, and still show the three other results.
#    Why: only the division is impossible with b = 0. 

def ask_number(prompt):
    """Ask until the user types something that is a valid number."""
    while True:
        text = input(prompt)
        try:
            return float(text)
        except ValueError:
            print(f"'{text}' is not a number, please try again.")


a = ask_number("First number: ")
b = ask_number("Second number: ")

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")

if b == 0:
    print(f"{a} / {b} = impossible: division by zero is not defined.")
else:
    print(f"{a} / {b} = {a / b}")