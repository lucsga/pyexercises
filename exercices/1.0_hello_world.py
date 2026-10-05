"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the message you want and how many times to show it.
# 2. Process: a loop runs COUNT times. Each time the loop runs it add 1 to the number till it reach the count number
# 3. Out: COUNT lines on the screen, numbered from 1, each holding the message.
# 4. My message, and why: "Please give me a summer" because i need a summer internship

MESSAGE = "Please give me a summer"
COUNT = 5  #the number of times to show the message

for number in range(1, COUNT + 1):
    print(number, MESSAGE)
