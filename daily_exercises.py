# by Allison Dixon
# last updated October 3, 2019
# unit four daily exercises
import random
# this program tells the user whether a number is even or odd
number = int(input("Give me a number."))
if (number % 2) == 1:
    print("That is an odd number.")
else:
    print("That is an even number.")


# this program prints true if num can be divided by check, and false if not
def is_divisible(num, check):
    if (num % check) == 0:
        print("True")
    else:
        print("False")


# this program sees if three sticks will be able to make a triangle
def is_triangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print("No")
    else:
        print("Yes")


def triangle_input():
    a = int(input("What is the length of the first stick?"))
    b = int(input("What is the length of the second stick?"))
    c = int(input("What is the length of the third stick?"))
    is_triangle(a, b, c)


# this program makes a rock-paper-scissors game
def computer():
    return random.choice(["rock", "paper", "scissors"])


def rock_paper_scissors():
    user_choice = input("Let's play rock-paper-scissors. Choose one!")
    computer_choice = computer()
    if computer_choice == "rock" and user_choice == "paper" or computer_choice == "paper" and \
            user_choice == "scissors" or computer_choice == "scissors" and user_choice == "rock":
        print("You won! Computer chose", computer_choice)
    elif computer_choice == user_choice:
        print("Tie! Computer chose", computer_choice, ". Go again.")
        rock_paper_scissors()
    else:
        print("You lost. Computer chose", computer_choice)


def caught_speeding(speed, birthday):
    if birthday or speed <= 60:
        print("Congratulations! No ticket!")
    elif 61 <= speed <= 80:
        print("Small ticket.")
    else:
        print("Big ticket.")


def main():
    num = float(input("Give me a number."))
    check = float(input("Give me another number."))
    is_divisible(num, check)
    triangle_input()
    rock_paper_scissors()
    caught_speeding(86, True)


main()
