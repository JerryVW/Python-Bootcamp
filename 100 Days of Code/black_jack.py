import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = True


# Get random cards
def deal_cards(deal, get_card):
    for i in range(get_card):
        cards_dealt = random.choice(cards)
        deal.append(cards_dealt)


# Sum up cards for total
def sum_of_cards(total_cards):
    return sum(total_cards)


# Get a card
def hit_card(player_cards, player_score):
    if choice == "h":
        deal_cards(player_cards, 1)
        if player_score > 21 and 11 in player_cards:
            player_cards.remove(11)
            player_cards.append(1)
        player_score = sum_of_cards(player_cards)
        print(f"    Your cards: {player_cards}, current score: {player_score}")


while play:

    want_another_card = False  # For another round of cards
    dealer = []
    player = []

    deal_cards(player, 2)
    deal_cards(dealer, 2)
    player_score = sum_of_cards(player)
    dealer_score = sum_of_cards(dealer)
    print(f"    Your cards: {player}, current score: {player_score}")
    print(f"    Dealer first card: {dealer[0]}")
    if player_score == 21 and dealer_score < 21:
        print("     You Win!!")
    elif player_score < 21 and dealer_score == 21:
        print("     You Lose!!")
    elif player_score == 21 and dealer_score == 21:
        print("     You Lose")

    # Take one more card
    while not want_another_card:
        choice = input("Type 'h' for hit or 's' to stand: ")
        want_another_card = hit_card(player, player_score)

    # Sum the scores
    dealer_score = sum_of_cards(dealer)
    player_score = sum_of_cards(player)

    # Giving dealer cards till it wins or busts
    while dealer_score < 17:
        deal_cards(dealer, 1)
        dealer_score = sum_of_cards(dealer)

    # Check comparisons for winner
    print(f"    Your final hand: {player}, final score is: {player_score}")
    print(f"    Dealer's final hand: {dealer}, final score is: {dealer_score}")

    if player_score > dealer_score and player_score < 21:
        print("     You Win!!")
    elif player_score < dealer_score and dealer_score < 21:
        print("     You Lose!!")
    elif player_score > dealer_score:
        print("     You Win!!")
    elif player_score < dealer_score:
        print("     You Lose!!")
    elif player_score == dealer_score:
        print("     It's a Draw!")

        # Checking to see if they want to play another game
    play_again = input(
        "Do you want to play a game oj BlackJack? 'y' for YES, 'n' for NO: "
    ).lower()

    if play_again == "y":
        dealer.clear()
        player.clear()
        play = True
    else:
        play = False
