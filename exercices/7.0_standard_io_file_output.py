"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.
"""

# 1. In: the user types 5 pieces of information about one advertising
#    campaign: its name, channel, month, budget and number of conversions.
#
# 2. Process:
#    - each answer is CHECKED; if it is not acceptable, the program explains
#      why and asks again for that field;
#    - the program checks whether the file already exists;
#    - it ADDS one line at the end of the file, without erasing anything.
#
# 3. Out, file name and columns:
#    File: campaigns.csv (separator ";", like 7.0_student_data.csv)
#    Columns: campaign_name;channel;month;budget_eur;conversions
#
# 4. Why these columns, and what this file is for:
#    - campaign_name: to identify the campaign
#    - channel:       to compare channels with each other
#    - month:         to see how spending changes over the year
#    - budget_eur:    to know how much was spent
#    - conversions:   to measure the result
#    With 200 rows, I would open it in Excel and compute the COST PER
#    CONVERSION of each channel (budget / conversions), then move the budget
#    towards the channels that perform best.
#
# My two decisions:
#    1. FIRST TIME (file does not exist yet, or is empty): write the header
#       line first, then the entry. Every other time: write only the entry.
#       That is how the file always has exactly ONE header line.
#    2. UNACCEPTABLE VALUE: refuse it, explain why, and ask again for that
#       field only. A wrong line is never written in the file. Rules:
#       - name and channel: not empty
#       - month: a whole number from 1 to 12
#       - budget: more than 0 (dot or comma accepted: 1200.50 or 1200,50)
#       - conversions: a whole number, 0 or more
#
# Key point: open(..., "a") means APPEND: add at the end of the file.
#    "w" (write) would ERASE the file every time: only the last entry would remain.
#
# Why the csv module: if the user types a ";" in a name, csv puts the value
#    between quotes automatically. Otherwise the ";" would shift the columns.


import csv
import os

FILE_NAME = "campaigns.csv"
COLUMNS = ["campaign_name", "channel", "month", "budget_eur", "conversions"]


def ask_text(question):
    """Ask until the answer is not empty, and return it."""
    while True:
        answer = input(question).strip()
        if answer != "":
            return answer
        print("This field cannot be empty, please try again.")


def ask_month(question):
    """Ask until the answer is a month number from 1 to 12, and return it."""
    while True:
        answer = input(question).strip()
        if answer.isdigit() and 1 <= int(answer) <= 12:
            return int(answer)
        print(f"'{answer}' is not a month number between 1 and 12, please try again.")


def ask_budget(question):
    """Ask until the answer is an amount above 0, and return it."""
    while True:
        # Accept the French comma: "1200,50" becomes "1200.50"
        answer = input(question).strip().replace(",", ".")
        try:
            amount = float(answer)
        except ValueError:
            print(f"'{answer}' is not an amount in euros, please try again.")
            continue
        if amount > 0:
            return amount
        print("The budget must be more than 0, please try again.")


def ask_conversions(question):
    """Ask until the answer is a whole number (0 or more), and return it."""
    while True:
        answer = input(question).strip()
        if answer.isdigit():
            return int(answer)
        print(f"'{answer}' is not a whole number (0 or more), please try again.")


# Collect one entry
campaign_name = ask_text("Campaign name: ")
channel = ask_text("Channel (e.g. Instagram Ads, Google Ads): ")
month = ask_month("Month (1-12): ")
budget = ask_budget("Budget in euros: ")
conversions = ask_conversions("Number of conversions: ")

# The header is needed only if the file does not exist yet, or is empty
file_needs_header = not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0

# "a" = append: add at the end, never erase what is already there
with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    if file_needs_header:
        writer.writerow(COLUMNS)
    writer.writerow([campaign_name, channel, month, budget, conversions])

print(f"Entry saved in {FILE_NAME}.")