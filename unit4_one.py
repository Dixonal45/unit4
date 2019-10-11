# by Allison Dixon
# last updated on October 9, 2019
# blackjack game

import random


def get_card():
    return random.randint(1, 10)


def print_starting_cards(card_1, card_2, total):
    print("You drew a", card_1, "and a", card_2)
    print("Your total is", total)


def another_card(card_3, new_user_total):
    another = input("Do you want another card? Enter 'y' for yes or 'n' for no.")
    if another == "y":
        print("You drew a", card_3, "and your new total is", new_user_total)


def dealer_cards():
    card_4 = get_card()
    card_5 = get_card()
    dealer_total = card_4 + card_5
    print("The dealer drew a", card_4, "and a", card_5)
    print("The dealer's total is", dealer_total)


def win_lose(new_user_total, user_total):
    if new_user_total > 21 or user_total > 21:
        print("You lost. Don't go to Vegas.")
    else:
        dealer_cards()


def main():
    card_1 = get_card()
    card_2 = get_card()
    user_total = card_1 + card_2
    print_starting_cards(card_1, card_2, user_total)
    card_3 = get_card()
    new_user_total = user_total + card_3
    another_card(card_3, new_user_total)
    win_lose(new_user_total, user_total)



main()
