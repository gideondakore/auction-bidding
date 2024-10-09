import os
auction_art = """
       ,
      /(  ___________
     |  >:===========`
      )(
"""

print(auction_art)
print("Welcome to the secret auction program")

response = True
bidders = {}
while response:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    res = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if res.lower() == "yes":
        os.system("cls" if os.name == "nt" else "clear")
    else:
        os.system("cls" if os.name == "nt" else "clear")
        max_val = max(bidders.values())
        # First method
        # for key in bidders:
        #     if max_val == bidders[key]:
        #         print(f"The winner is {key.lower().capitalize()} with a bid of ${max_val}.")
        #         response = False
        # Second method
        max_bidder_name = max(bidders, key=bidders.get)
        print(f"The winner is {max_bidder_name.lower().capitalize()} with a bid of ${max_val}.")
        response = False


