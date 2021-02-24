import Milestone_Project_2_Classes
from os import system, name
from time import sleep

# Determine amount user wants to bet for that round
def bet(money: int) -> int:
    while True:
        try:
            bet_amount = int(input("Enter bet amount for this round: $"))

            if bet_amount > money:
                print("Bet amount is greater than your chips! Enter a valid bet amount.")
                continue
            else:
                return bet_amount
        except:
            print("Invalid entry! Please enter a valid number for your bet.")
            continue

# Establishing initial funds for the player
def chips() -> int:
    while True:
        try:
            money = int(input("Enter player balance: $"))
        except:
            print("Invalid entry! Please enter a valid number to represent your balance.")
            continue
        else:
            return money

# Prompting to see if user wants to hit or not
def hit_check() -> str:
    while True:
        try:
            hit = input("Would you like to hit? (Y\\N): ")
            hit = hit.capitalize()

            if hit == 'Y' or hit == 'N':
                return hit
            else:
                raise ValueError()
        except:
            print("Invalid entry! Please enter Y or N for your decision to hit.")
            continue

# Prompting to play again or end program
def play_again() -> str:
    while True:
        try:
            play = input("Would you like to play again? (Y\\N): ")
            play = play.capitalize()

            if play == 'Y' or play == 'N':
                return play
            else:
                raise ValueError()
        except:
            print("Invalid entry! Please enter Y or N for your decision to play again.")
            continue

# Clearing output
def clear() -> None:
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    game_start = True
    round_num = 0

    # Creating dealer and player objects
    dealer = Milestone_Project_2_Classes.Hand()
    player = Milestone_Project_2_Classes.Player()

    # Retrieving player name and their gambling funds
    player.name = input("Enter player name: ")
    player.money = chips()

    while game_start == True:
        new_round = None
        exit_check = True

        deck = Milestone_Project_2_Classes.Deck()
        deck.shuffle()

        clear()
        player.clear_hand()
        dealer.clear_hand()

        print(f"Current funds: ${player.money}")

        round_num += 1

        # Check if user has any money left to gamble
        if player.money == 0:
            print("Out of money! GAME OVER!!!")
            game_start = False
            break
        else:
            pass

        # Print the round number and ask user for their bet amount
        print(f"Round {round_num}")
        player.bet = bet(player.money)
        print()

        # Dealing 2 cards to dealer and player
        for card_dealing in range(0,2):
            dealer.player_hand(deck.deal())
            player.player_hand(deck.deal())

        # Revealing one dealer card and the player's hand
        print(f"One revealed Dealer card: {dealer.hand[0]} ({Milestone_Project_2_Classes.values[dealer.hand[0].rank]})")
        print(f"Player hand: {player.hand[0]}, {player.hand[1]} ({player.value})")

        # Count the aces in the hands of each player
        player.count_ace()
        dealer.count_ace()

        # Determine if user wants to hit given their current hand
        check_hitting = True
        while check_hitting == True:
            print()
            hit = hit_check()

            # Give user another card if they hit, reprint their hand
            if hit == 'Y':
                player.player_hand(deck.deal())
                player.count_ace()
                player.adjust_ace()
                print("New player hand: ", end='')

                for card_sel in range(0, len(player.hand)):
                    if card_sel == len(player.hand)-1:
                        print(f"{player.hand[card_sel]} ({player.value})")
                    else:
                        print(player.hand[card_sel], end=', ')

                # If user's hand value is greater than 21, report the loss
                if player.value > 21:
                    print("BUST! Dealer wins.")
                    player.new_amount('L')
                    print()
                    print("Current funds: ${}".format(player.money))
                    dealer.value = 1000
                    exit_check = False
                    check_hitting = False
                else:
                    continue
            else:
                check_hitting = False

        if exit_check == False:
            new_round = play_again()
            continue
        else:
            pass

        # Reveal both Dealer's cards
        print(f"\nBoth Dealer's cards revealed: {dealer.hand[0]}, {dealer.hand[1]} ({dealer.value})")

        # Check if the two cards are greater or equal to the soft cap (17) and report results
        if dealer.value >= 17:

            # Adjust values for aces
            dealer.adjust_ace()

            if dealer.value > player.value:
                print("Dealer wins!")
                player.new_amount('L')
                print()
                print("Current funds: ${}".format(player.money))
                new_round = play_again()
                dealer.value = 1000

            elif dealer.value == player.value:
                print("Draw! No money lost or gained.")
                print()
                print("Current funds: ${}".format(player.money))
                new_round = play_again()
                dealer.value = 1000

            else:
                print("Player wins!")
                player.new_amount('W')
                print()
                print("Current funds: ${}".format(player.money))
                new_round = play_again()
                dealer.value = 1000

        else:
            pass

        # Loop for the dealer to continually hit until they reach or surpass the soft cap (17)
        while dealer.value <= 17:
            dealer.player_hand(deck.deal())
            dealer.count_ace()
            dealer.adjust_ace()

            #print(f'{dealer.value}#1')

            # Case for dealer to bust
            if dealer.value > 21:
                print("New dealer hand: ", end='')

                for card_sel in range(0, len(dealer.hand)):
                    if card_sel == len(dealer.hand)-1:
                        print(f"{dealer.hand[card_sel]} ({dealer.value})")
                        sleep(1)
                    else:
                        print(dealer.hand[card_sel], end=', ')
                        sleep(1)
                print(f"Dealer BUSTS! {player.name} has won.")
                player.new_amount('W')
                print()
                print("Current funds: ${}".format(player.money))
                new_round = play_again()
                dealer.value = 1000

            # Case for dealer to continue hitting
            elif dealer.value < 17:
                print("New dealer hand: ", end='')

                for card_sel in range(0, len(dealer.hand)):
                    if card_sel == len(dealer.hand)-1:
                        print(f"{dealer.hand[card_sel]} ({dealer.value})")
                    else:
                        print(dealer.hand[card_sel], end=', ')
                continue

            # Case for dealer to win over player based on value
            elif dealer.value > 17 and dealer.value > player.value:
                print("New dealer hand: ", end='')

                for card_sel in range(0, len(dealer.hand)):
                    if card_sel == len(dealer.hand)-1:
                        print(f"{dealer.hand[card_sel]} ({dealer.value})")
                        sleep(1)
                    else:
                        print(dealer.hand[card_sel], end=', ')
                        sleep(1)

                #print(f'{dealer.value}#3')
                print("Dealer has won!")
                player.new_amount('L')
                print()
                print("Current funds: ${}".format(player.money))
                new_round = play_again()
                dealer.value = 1000

            # Case for a draw between dealer and player
            elif dealer.value > 17 and dealer.value == player.value:
                print("New dealer hand: ", end='')

                for card_sel in range(0, len(dealer.hand)):
                    if card_sel == len(dealer.hand)-1:
                        print(f"{dealer.hand[card_sel]} ({dealer.value})")
                        sleep(1)
                    else:
                        print(dealer.hand[card_sel], end=', ')
                        sleep(1)

                #print(f'{dealer.value}#4')
                print("Draw! No money lost or gained.")
                print()
                print("Current funds: ${}".format(player.money))
                new_round = play_again()
                dealer.value = 1000

            # Case for player winning over dealer based on hand value
            elif dealer.value > 17 and dealer.value < player.value:
                print("New dealer hand: ", end='')

                for card_sel in range(0, len(dealer.hand)):
                    if card_sel == len(dealer.hand)-1:
                        print(f"{dealer.hand[card_sel]} ({dealer.value})")
                        sleep(1)
                    else:
                        print(dealer.hand[card_sel], end=', ')
                        sleep(1)

                #print(f'{dealer.value}#5')
                print("Player wins!")
                player.new_amount('W')
                print()
                print("Current funds: ${}".format(player.money))
                new_round = play_again()
                dealer.value = 1000

            else:
                pass

        # Condition for a new round
        if new_round ==  'Y':
            continue
        # End the game
        elif new_round == 'N':
            game_start = False

        else:
            break

if __name__ == '__main__':
    main()
