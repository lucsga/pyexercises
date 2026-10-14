"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Spaces or a tab at the start or end of some lines:
#   "  Lucas Martin", "Giulia Rossi  ", a TAB before "Karim Benali", "Emma  Petit "
# - Empty lines (lines 4 and 15), and one line with only spaces (line 9)
# - Inconsistent capitals: "SOPHIE BERNARD", "OLIVIER MOREAU" (all caps),
#   "thomas leroy", "lucas martin" (all lowercase)
# - Several spaces between words: "Amina   Diallo", "Emma  Petit"
# - Two formats: most lines are "First Last", but "Chen, Wei" and
#   "Schmidt, Anna" are "Last, First"
# - Duplicates, some hidden by spaces or capitals: "Marie Dupont" twice,
#   "Lucas Martin" / "lucas martin", "Giulia Rossi" / "Giulia Rossi  "
# - A last name in two words: "Lucas van Dijk" -> last name is "van Dijk"

# 1. In: names.txt, 20 lines. It is only READ ("r"), never modified.
#
# 2. Process, problem by problem:
#    - spaces/tab at both ends -> .strip() removes them
#    - empty lines             -> after .strip() they are "", so they are skipped
#    - capitals                -> each word is rewritten: "SOPHIE" -> "Sophie"
#    - several spaces          -> .split() with no argument splits on any
#                                 number of spaces
#    - "Last, First" format    -> if there is a comma, what is BEFORE it is
#                                 the last name, what is AFTER it is the first name
#    - duplicates              -> names are compared AFTER cleaning, so
#                                 "lucas martin" = "Lucas Martin"; only the first is kept
#    - particles (van, de...)  -> kept in lowercase, part of the last name
#
# 3. Out: a NEW file, names_sorted.txt: 14 names, "First Last", one per line, sorted by last name.
#
# 4. How I decide which word is the last name:
#    - with a comma ("Chen, Wei"): the last name is BEFORE the comma;
#    - without a comma: the FIRST word is the first name, EVERYTHING ELSE
#      is the last name. So "Lucas van Dijk" -> first "Lucas", last "van Dijk".
#    Same last name -> sorted by first name. Capitals are ignored when sorting.
#    Decision: "van Dijk" is sorted under V (in the Netherlands it would be
#    under D). I sort on the full last name as it is written: simplest rule.
#


INPUT_FILE = "names.txt"
OUTPUT_FILE = "names_sorted.txt"

# Small words that belong to a last name and stay in lowercase
PARTICLES = ["van", "von", "de", "du", "der", "da", "di", "le", "la"]


def fix_case(word):
    """Return the word with a capital first letter (particles stay lowercase)."""
    if word.lower() in PARTICLES:
        return word.lower()
    return word.capitalize()


def fix_case_all(words):
    """Return the words joined by single spaces, each with the right capitals."""
    fixed = []
    for word in words:
        fixed.append(fix_case(word))
    return " ".join(fixed)


def clean_line(line):
    """Return (first_name, last_name) for one line, or None if the line is empty."""
    line = line.strip()
    if line == "":
        return None

    if "," in line:
        # "Last, First" format
        last_part, first_part = line.split(",", 1)
        first_words = first_part.split()
        last_words = last_part.split()
    else:
        # "First Last" format: first word = first name, the rest = last name
        words = line.split()
        first_words = words[:1]
        last_words = words[1:]

    first_name = fix_case_all(first_words)
    last_name = fix_case_all(last_words)
    return (first_name, last_name)


def sort_key(person):
    """Return what to sort on: last name first, then first name, ignoring capitals."""
    first_name, last_name = person
    return (last_name.lower(), first_name.lower())


# Read the original file ("r" = read only, it is never modified)
with open(INPUT_FILE, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Clean every line, skip empty lines and duplicates
people = []
for line in lines:
    person = clean_line(line)
    if person is not None and person not in people:
        people.append(person)

# Sort by last name
people = sorted(people, key=sort_key)

# Write the result to a NEW file
with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    for first_name, last_name in people:
        file.write(f"{first_name} {last_name}\n")

print(f"{len(lines)} lines read, {len(people)} names written to {OUTPUT_FILE}.")