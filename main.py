import os
from secret_auction_art import creator, logo
from secret_auction_methods import is_float


data = []
end_bidder_loop = False
winner = ''

print(f"{logo}\nWelcome to the secret auction program.")

while not end_bidder_loop:
  name = input("What is your name? ")
  while len(name) == 0:

    name = input("What is your name? ")

  bid = input("What is your bid? $")

  while not (is_float(bid) or bid.isnumeric()):
    bid = input("Wrong Input, please add a number as a bid? $")

  data.append({"name": name, "bid": bid})

  anotherBidder = input(
      "Are there any other bidder? Type 'yes' or 'no'.\n").lower()

  while not (anotherBidder == "yes" or anotherBidder == "no"):
    anotherBidder = input(
        "Wrong input, Are there any other bidder? Type 'yes' or 'no'.\n"
    ).lower()

  if anotherBidder == "no":
    end_bidder_loop = True
  else:
    os.system('CLS')

os.system('CLS')
print(logo)
winner = data[0]
for item in data:
  if float(item['bid']) > float(winner['bid']):
    winner = item

print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")
print(f"\nCreated by:\n{creator}")
