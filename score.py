"""
CP1404/CP5632 - Practical
Broken program to determine score status

function_main()
  get score
  determine_status(score)
  get random_score
  display "Random score generated is {random_score}"
  determine_status(random_score)

function determine_status(score)
    if score < 0 or score > 100
        display "Invalid score"
    else score >= 90
        display "Excellent"
    else score >= 50
        display "Pass"
    else
        print("Bad")
"""

import random
# TODO: Fix this!
LOW_SCORE = 0
HIGH_SCORE = 100
PASS_SCORE = 50
EXCELLENT_SCORE = 90


def main():
    score = float(input("Enter score: "))
    determine_status(score)
    random_score = random.randint(LOW_SCORE, HIGH_SCORE)
    print(f"Random score generated is {random_score}")
    determine_status(random_score)


def determine_status(score):
    if score < LOW_SCORE or score > HIGH_SCORE:
        print("Invalid score")
    elif score >= EXCELLENT_SCORE:
        print("Excellent")
    elif score >= PASS_SCORE:
        print("Pass")
    else:
        print("Bad")


main()
