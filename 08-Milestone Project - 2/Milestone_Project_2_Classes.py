'''
Blackjack game with 1 player vs a computer dealer implemented with object-oriented programming
'''

import random

# Global variables defining card information used for the game
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

# Class for creating individual card objects
class Card:

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

# Class for game deck object
class Deck:
    def __init__(self) -> None:
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def __str__(self) -> str:
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self) -> None:
        random.shuffle(self.all_cards)

    def deal(self) -> str:
        return self.all_cards.pop()

class Hand:
    def __init__(self) -> None:
        self.hand = []
        self.value = 0
        self.aces = 0

    def player_hand(self, card: Card) -> None:
        self.hand.append(card)
        self.value = 0

        for card in range(0, len(self.hand)):
            num = values[self.hand[card].rank]
            self.value += num

    def clear_hand(self) -> None:
        self.hand = []
        self.value = 0
        self.aces = 0

    def count_ace(self) -> None:
        self.aces = 0
        for cards in self.hand:
            if cards.rank == 'Ace':
                self.aces += 1
            else:
                pass

    def adjust_ace(self) -> None:
        if self.value > 21 and self.aces > 0:
            for ace in range(0, self.aces):
            #if self.value > 21 and self.aces > 0:
                self.value -= 10
            #else:
                #pass
        else:
            pass

class Player(Hand):
    def __init__(self) -> None:
        self.name = ''
        self.money = 0
        self.hand = []
        self.value = 0
        self.bet = 0
        self.aces = 0

    def new_amount(self, outcome: str) -> None:
        if outcome.capitalize() == 'W':
            self.money = self.money + self.bet*2
        else:
            self.money = self.money - self.bet

        self.bet = 0

if __name__ == '__main__':
    for x in range(1,1):
        print("Test")
