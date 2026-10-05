"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two answers typed by the user: a campaign name (text) and its budget in euros (number).
# 2. Process: it takes the two answers write by the user and it use them in a sentence
# 3. Out: one sentence with the campaign name, the budget, and the budget increased by 1.
# 4. My two fields, and what I would do with them: first ther is the campain name, and then the budget. I would use them to display a sentence with the campaign name, the budget, and the budget increased by 1.

campaign = input("Campaign name: ")
budget = float(input("Budget in euros: ")) 

new_budget = budget + 1

print("The campaign", campaign, "has a budget of", budget, "euros, and", new_budget,
      "euros with 1 more.")


