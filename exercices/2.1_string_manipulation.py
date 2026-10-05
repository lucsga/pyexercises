"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one sentence typed by the user
# 2. Process: the sentence is transformed four times. Each transformation starts from the original text, first without any spaces, then lowercase, then capital on each word and slug.
# 3. Out: four lines, one per transformation.
# 4. My four transformations, and when each is useful:
#    - replace(" ", ""): removes every space in the sentence. Useful to build a compact code.
#    - lower(): all lowercase.
#    - title(): a capital on each word. 
#    - replace(" ", "-"): spaces become hyphens.

sentence = input("Type a sentence: ")

no_spaces = sentence.replace(" ", "")
lowercase = sentence.lower()
titled = sentence.title()
slug = sentence.strip().lower().replace(" ", "-")

print("Without any spaces       :", no_spaces)
print("Lowercase                 :", lowercase)
print("Capital on each word      :", titled)
print("Slug                      :", slug)
