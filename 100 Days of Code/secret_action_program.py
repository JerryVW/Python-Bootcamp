auction_participants = {}

print("Welcome to the silent auction!")

continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = int(input("How much would you like to bid? $"))
    auction_participants[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n"
    ).lower()
    if should_continue == "no":
        continue_bidding = False
    elif should_continue == "yes":
        print("\n" * 25)


highest_bidder = max(auction_participants, key=auction_participants.get)
print(
    f"The winner is {highest_bidder} with a bid of ${auction_participants[highest_bidder]}"
)
