print("Welcome to the secret auction program. ")
name = input("Enter your name. ")
bid = (input("And how much will you be bidding? "))

bidders_database = {}

def silent_bidding_methodoly(persons_name, their_bid):
  bidders_database[persons_name] = int(their_bid)
  
  values_list = list(bidders_database.values())
  keys_list = list(bidders_database.keys())
  heightest_bidder_index = values_list.index(max(values_list))


  more_bidders = input("Is anyone else bidding beside you? Please type 'yes' or 'no' " ).lower()
  while more_bidders == "no":
    print(f"The winner of the auction is {keys_list[heightest_bidder_index]} with a bid of ${values_list[heightest_bidder_index]}.")
    break
  else:
    name = input("Enter your name. ")
    bid = input("And how much will you be bidding? ")
    silent_bidding_methodoly(persons_name=name, their_bid=bid)

silent_bidding_methodoly(persons_name=name, their_bid=bid)

