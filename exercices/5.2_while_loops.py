"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.
"""

# 1. In: answers typed by the user, one per attempt: either a campaign budget in euros, or the word "done" to finish.
#
# 2. Process: each answer is cleaned with .strip().lower()
#    (.strip() removes spaces at both ends, .lower() puts it in lowercase).
#    - "done" -> leave the loop (break);
#    - an amount (dot or comma, e.g. 1200.50 or 1200,50) above 0 -> recorded;
#    - anything else (text, 0, negative amount) -> counted as invalid, and the loop goes on.
#    The comma is replaced by a dot before converting, because Python only understands "1200.50", not "1200,50".
#
# 3. Out: a summary: why the loop stopped (user or limit), the budgets recorded, how many, their total, and the number of invalid answers.
#
# 4. My stop condition, my attempt limit, my summary:
#    - Stop condition: the user types "done".
#    - Safety limit: 5 attempts maximum. When it is reached, the program stops by itself and still shows the summary of what was typed, so nothing is lost.
#    - "Done", "DONE" and "  done  " are accepted as "done": someone typing "Done" clearly wants to stop, refusing it would be absurd.
#    - An invalid answer COUNTS as an attempt. Otherwise someone typing nonsense could keep the program running for ever.
#    - A budget must be more than 0: a negative or zero budget makes no sense.
#


MAX_ATTEMPTS = 5
STOP_WORD = "done"

amounts = []
invalid_answers = 0
attempts = 0
stopped_by_user = False

print("Enter the September budget of each campaign in euros.")
print(f"Type '{STOP_WORD}' when you have finished (maximum {MAX_ATTEMPTS} attempts).")

while attempts < MAX_ATTEMPTS:
    attempts = attempts + 1
    answer = input(f"Attempt {attempts}/{MAX_ATTEMPTS}: ")
    cleaned = answer.strip().lower()

    # Stop condition
    if cleaned == STOP_WORD:
        stopped_by_user = True
        break

    # Accept the French comma: "1200,50" becomes "1200.50"
    cleaned = cleaned.replace(",", ".")

    # Try to convert the answer into a number
    try:
        amount = float(cleaned)
    except ValueError:
        invalid_answers = invalid_answers + 1
        print(f"'{answer}' is not an amount in euros, it is not counted.")
        continue  # go straight to the next attempt

    # A budget must be more than 0
    if amount > 0:
        amounts.append(amount)
    else:
        invalid_answers = invalid_answers + 1
        print(f"'{answer}' must be more than 0, it is not counted.")

# Summary
print("\n--- Summary ---")
if stopped_by_user:
    print(f"Stopped by the user after {attempts} attempt(s).")
else:
    print(f"Limit of {MAX_ATTEMPTS} attempts reached: the program stopped by itself.")

print("Budgets recorded:", amounts)
print("Number of budgets:", len(amounts))
print(f"Total: {sum(amounts):.2f} EUR")
print("Invalid answers:", invalid_answers)