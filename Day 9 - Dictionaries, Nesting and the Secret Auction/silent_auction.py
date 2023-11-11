import os
from logo import logo

print(logo)
print("Welcome to the secret auction program!")

list_of_bidders = []

while True:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    list_of_bidders.append({"name": name, "bid": bid})
    flag = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if flag == 'yes':
        os.system('cls||clear')
    else:
        break

bid_winner = {}
max_bid = 0

for bidder in list_of_bidders:
    if bidder["bid"] > max_bid:
        max_bid = bidder["bid"]
        bid_winner = bidder

print(f"The winner is {bid_winner['name']} with a bid of ${bid_winner['bid']}.")