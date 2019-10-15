# by Allison Dixon
# last updated on October 15, 2019
# blackjack game

import random


def get_card():
    """
    This function generates a random card between values 1-10
    :return: A random card between values 1-10
    """
    return random.randint(1, 10)


def print_starting_cards(card_1, card_2, total):
    """
    This function prints the user's two starting cards and the total of those cards
    :param card_1: first random card
    :param card_2: second random card
    :param total: first random card + second random card
    :return: nothing
    """
    print("You drew a", card_1, "and a", card_2)
    print("Your total is", total)


def main():
    card_1 = get_card()
    card_2 = get_card()
    user_total = card_1 + card_2
    print_starting_cards(card_1, card_2, user_total)
    another = input("Do you want another card? Enter 'y' for yes or 'n' for no.")
    if another == "y":
        card_3 = get_card()
        user_total = user_total + card_3
        print("You drew a", card_3, "and your new total is", user_total)

    if user_total > 21:
        print("You lost. Don't go to Vegas.")
    else:
        card_4 = get_card()
        card_5 = get_card()
        dealer_total = card_4 + card_5
        print("The dealer drew a", card_4, "and a", card_5)
        print("The dealer's total is", dealer_total)
        if dealer_total >= user_total:
            print("You lose. Don't go to Vegas.")
        else:
            print("You win!")


main()
