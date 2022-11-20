"""
CP1404 / CP5632 - Practical
Pseudocode for temperature conversion

function main()
    display menu
    get choice
    while choice != "Q"
       if choice == "C"
         fahrenheit_to_celsius
       else if choice == "F"
         celsius_to_fahrenheit
       else
           display "invalid option"
       display menu
       get choice
    display "Thank you"


function fahrenheit_to_celsius()
    get celsius
    fahrenheit = celsius * 9.0 / 5 + 32
    display fahrenheit


function celsius_to_fahrenheit()
    get fahrenheit
    celsius = 5 / 9 * (fahrenheit - 32)
    display celsius
"""


def main():
    menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_to_fahrenheit()
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
            fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


def celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()
