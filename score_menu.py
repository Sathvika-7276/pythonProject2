"""
function main()
  display menu
  get score
  get user_choice
  while user_choice != "Q"
    if user_choice == "G"
        get score
    else user_choice == "P"
        determine_status(score)
    else user_choice == "S"
        print_asterisk(score)
    else
        print("Invalid choice")
    display(menu)
    get user_choice
  display "Thank you"

function get_valid_number(prompt, low, high)
    get number
    while number < low or number > high
        display "Invalid input"
        get number
    return number

function determine_status(score)
    if score < 0 or score > 100
        display "Invalid score"
    else score >= 90:
        display "Excellent"
    else score >= 50
        display "Pass"
    else
        display "Bad"

function print_asterisk(score)
    display("*" * int(score))
"""

LOWEST_SCORE = 0
HIGHEST_SCORE = 100
PASS_SCORE = 50
EXCELLENT_SCORE = 90


def main():
    menu = """(G)et a valid score 
(P)rint result 
(S)how stars 
(Q)uit """
    print(menu)
    score = get_valid_number("Score: ", LOWEST_SCORE, HIGHEST_SCORE)
    user_choice = input(">>>").upper()
    while user_choice != "Q":
        if user_choice == "G":
            score = get_valid_number("Score: ", LOWEST_SCORE, HIGHEST_SCORE)
        elif user_choice == "P":
            determine_status(score)
        elif user_choice == "S":
            print_asterisk(score)
        else:
            print("Invalid choice")
        print(menu)
        user_choice = input(">>>").upper()
    print("Thank you")


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def determine_status(score):
    if score < LOWEST_SCORE or score > HIGHEST_SCORE:
        print("Invalid score")
    elif score >= EXCELLENT_SCORE:
        print("Excellent")
    elif score >= PASS_SCORE:
        print("Pass")
    else:
        print("Bad")


def print_asterisk(score):
    print("*" * int(score))


main()
