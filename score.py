"""
CP1404/CP5632 - Practical
Broken program to determine score status

get score
if score < 0 or score > 100:
  display "Invalid score"
else score >= 90
  display "Excellent"
else score >= 50
  display "Pass"
else
  display "Bad"
"""

# TODO: Fix this!
LOW_SCORE = 0
HIGH_SCORE = 100
PASS_SCORE = 50
EXCELLENT_SCORE = 90

score = float(input("Enter score: "))
if score < LOW_SCORE or score > HIGH_SCORE:
    print("Invalid score")
elif score >= EXCELLENT_SCORE:
    print("Excellent")
elif score >= PASS_SCORE:
    print("Pass")
else:
    print("Bad")
