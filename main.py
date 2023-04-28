"""_author_ = Christopher Fox """
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9,
        10, 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J',
        'Q', 'K', 'A']


def converter(card):
    """This function converts face card Jack Queen and King to the value 10

    :param card: Represents the card it is converting
    :return: Returns 10 if a face card is detected or the same value if it
    is an integer
    """
    if card == 'Q' or card == 'K' or card == 'J':
        return 10
    elif card == 'A':
        return 11
    else:
        return card


def preliminary():
    """
This is the preliminary function for all requirements, it will have a warning
since I am not using any of the varibles in this function.
    """
    y = 5 ** 5
    p = 5 - 5
    m = 5 // 5
    n = 5 / 5
    z = 5 % 5


def main():
    """
This is the main function that runs the game from start to end
    """
    preliminary()
    print('*' * 8, 'Welcome to BlackJack!', '*' * 8, )
    # Dealing player
    card1 = (random.choice(deck))
    deck.remove(card1)
    card2 = (random.choice(deck))
    deck.remove(card2)
    # Finding if split is possible
    if card1 == card2:
        same = True
    else:
        same = False

    if card1 == 'A' or card2 == 'A':
        ace_check = 1
    else:
        ace_check = 0
    print('Your cards are ', card1, card2)

    # Dealing dealer
    card3 = (random.choice(deck))
    deck.remove(card3)
    card4 = (random.choice(deck))
    deck.remove(card4)
    print('Dealer card is a ', card3)
    card1 = converter(card1)
    card2 = converter(card2)
    player_total = card1 + card2
    # If player has an ace, show both possibilities
    if ace_check > 0 and player_total < 21:
        player_total2 = player_total - 10
        print('Your total is', player_total, 'or', player_total2)
    # If player gets 2 Aces, one ace turns into 1
    elif player_total == 22:
        player_total = 12
        print('Your total is', player_total)
    else:
        print('Your total is', player_total)

    if player_total == 21:
        print('You got blackjack!')
        black_jack = 'natural'
    else:
        black_jack = 'no'

    if same is True:
        split = input('Would you like to split? ')
        if split == 'Yes' or split == 'yes':
            if card1 == 'A':
                player_total = 11
                split_total = 0
                choice = True
                while choice is True:
                    new_card = (random.choice(deck))
                    deck.remove(new_card)
                    print('Your next card is a ', new_card)
                    if new_card == 'A':
                        ace_check += 1
                    new_card = converter(new_card)
                    player_total += new_card
                    if player_total > 21 and ace_check > 0:
                        player_total -= 10
                        ace_check -= 1
                    print('Your total is', player_total)
                    # If player got blackjack
                    if player_total == 21:
                        print('You got blackjack!')
                        choice = False
                    elif split_total > 0:
                        if player_total < split_total:
                            player_total = split_total
                            choice = False
                    else:
                        split_total = player_total
                        player_total = 11
                        choice = True
            else:
                player_total = card1
                split_total = card2
                choice = True
        else:
            split = 'no'
            split_total = 0
            player_option = input('Would you like to hit? ')
            if player_option == 'Yes' or player_option == 'yes':
                choice = True
            else:
                choice = False
    else:
        split = 'no'
        split_total = 0
        if player_total != 21:
            player_option = input('Would you like to hit? ')
            if player_option == 'Yes' or player_option == 'yes':
                choice = True
            else:
                choice = False
        else:
            choice = False

    while choice is True:
        new_card = (random.choice(deck))
        deck.remove(new_card)
        print('Your next card is a ', new_card)
        if new_card == 'A':
            ace_check += 1
        new_card = converter(new_card)
        player_total += new_card
        # If the players total is over 21 and the player has an ace than
        # the computer will subtract 10 turning ace from an 11 to a 1
        if player_total > 21 and ace_check > 0:
            player_total -= 10
            ace_check -= 1
        # If the player has an ace, but it doesn't exceed 21 you show
        # both options
        if ace_check > 0 and player_total < 21:
            player_total2 = player_total - 10
            print('Your total is', player_total, 'or', player_total2)
        else:
            print('Your total is', player_total)
        # If player got blackjack
        if player_total == 21:
            print('You got blackjack!')
            choice = False
        else:
            # If player split
            if split != 'no':
                # If player is on first card of split
                if split_total == card2:
                    # If players first split < 21 they can hit
                    if player_total < 21:
                        player_option = input('Would you like to hit? ')
                        if player_option == 'Yes' or player_option == 'yes':
                            choice = True
                        else:
                            # If they don't want to hit than moves on to
                            # 2nd split
                            # card
                            split_total = player_total
                            player_total = card2
                            choice = True
                    # If player total is > 21
                    else:
                        print('You busted!')
                        split_total = player_total
                        player_total = card2
                        choice = True
                # If player is on 2nd card of split
                else:
                    # If player busted both hands
                    if player_total > 21 and split_total > 21:
                        print('You busted!')
                        quit()
                    # If player busted 2nd hand but 1st is still playable
                    elif player_total > 21:
                        print('You busted this hand!')
                        player_total = split_total
                        print('Your first total:', player_total)
                        choice = False
                    elif player_total < 21:
                        player_option = input('Would you like to hit? ')
                        if player_option == 'Yes' or player_option == 'yes':
                            choice = True
                        else:
                            choice = False
                            # Assign greater total that > 21 to player_total
                            if split_total > player_total:
                                player_total = split_total
            else:
                # Finding if player busts
                if player_total > 21:
                    print('You busted!')
                    quit()
                else:
                    option = input('Would you like to hit? ')
                    if option == 'Yes' or option == 'yes':
                        choice = True
                    else:
                        choice = False

    print('')
    print("Dealer's turn")
    print("Dealer's second card is a ", card4)
    if card3 == 'A' or card4 == 'A':
        ace_check = 1
    else:
        ace_check = 0
    card3 = converter(card3)
    card4 = converter(card4)
    dealer_total = card3 + card4
    if dealer_total == 22:
        dealer_total = 12
    print('Dealer total is', dealer_total)

    if black_jack == 'natural' and dealer_total != 21:
        print('You win!')
        quit()

    if dealer_total < 17:
        dealer_choice = True
    else:
        dealer_choice = False

    while dealer_choice is True:
        new_card = (random.choice(deck))
        deck.remove(new_card)
        print('Dealer hits and gets a ', new_card)
        if new_card == 'A':
            ace_check += 1
        new_card = converter(new_card)
        dealer_total += new_card
        if dealer_total > 21 and ace_check > 0:
            dealer_total -= 10
            ace_check -= 1
        print('Dealer total is', dealer_total)
        # Finding if player busts
        if dealer_total > 21:
            print('Dealer busted! You Win')
            quit()
        elif dealer_total == 21:
            print('Dealer got blackjack!')
            dealer_choice = False
        if dealer_total > 16:
            dealer_choice = False

    if dealer_total > player_total:
        print('Dealer:', dealer_total, 'You:', player_total)
        print('Dealer wins!')
    else:
        if dealer_total == player_total:
            print('Dealer:', dealer_total, 'You:', player_total)
            print('Draw!')
        else:
            print('Dealer:', dealer_total, 'You:', player_total)
            print('You win!')


main()
