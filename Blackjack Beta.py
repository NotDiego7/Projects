import random
cards = {
    "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "king": 10, "queen": 10, "jack": 10,
    "ace_eleven": 11, # Can work simple arithmetic to get ace_one when needed
}

dealer_cards = []
player_cards = []
end_game = False


def get_random_card():
    global dealer_score, player_score
    cards_keys_list = list(cards.keys())
    cards_random_key = random.choice(cards_keys_list)
    card = cards.get(cards_random_key)
    return card



def dealer_under_seventeen_else_dealer_stats(): 
    global dealer_score, dealer_cards
    while dealer_score < 17:
        card = get_random_card()
        if card == 11 and dealer_score > 10:
            card = 1
        dealer_cards.append(card)
        dealer_score = sum(dealer_cards)
    if len(dealer_cards) > 2: 
        return f"\nDealer was forced to hit since he was below the 17 score threshold\nDealer's hand: {dealer_cards}\nDealer's score: {dealer_score}"
    return f"\nDealer's hand: {dealer_cards}\nDealer's score: {dealer_score}"


def stand_functionality(player_score_param, dealer_score_param):                                                                                                    
    global player_score, dealer_score, player_cards, end_game
    
    print(dealer_under_seventeen_else_dealer_stats())
    
    if dealer_score > player_score and dealer_score <= 21:
        end_game = True
        return f"\nDealer wins!\nDealer's score: {dealer_score}\nYour score: {player_score}"
    elif player_score > dealer_score:
        end_game = True
        return f"\nYou win!\nDealer's score: {dealer_score}\nYour score: {player_score}"
    elif player_score == dealer_score:
        end_game = True
        return f"\nIt's a tie!\nDealer's score: {dealer_score}\nYour score: {player_score}"
    else:
        end_game = True
        return f"Dealer busted!\nYou win!\nYour score: {player_score}"



def hit_functionality(player_score_param, dealer_score_param, dealer_cards_param):
    global player_score, dealer_score, player_cards, end_game
    card = get_random_card()
    if card == 11 and player_score > 10:
        card = 1
    player_cards.append(card)
    player_score = sum(player_cards)
    print(f"\nYour hand: {player_cards}\nYour score: {player_score}")
    if player_score > 21:
        end_game = True
        print(f"\nBusted! You lose!\nYour score: {player_score}")
        print(dealer_under_seventeen_else_dealer_stats())
        if dealer_score > 21:
            print(f"\nDealer also busted!")
    else:
        while player_score <= 21 and not end_game:
            main_flow()



def main_flow():
    hit_stand_prompt = input("\nIf you want to 'hit', type 'hit'; otherwise, type 'stand'. ").lower()
    if hit_stand_prompt == "stand":
        print(stand_functionality(player_score, dealer_score))
    elif hit_stand_prompt == "hit":
        print(hit_functionality(player_score, dealer_score, dealer_cards))


play_prompt = input("Do you want to play a game of BlackJack? Type 'yes' or 'no' ").lower()
if play_prompt == 'yes':
    print("Welcome to BlackJack.")
    print("You will be dealt two cards:\n")
    
    for i in range(2):
        player_cards.append(get_random_card())
        dealer_cards.append(get_random_card())
    player_score = sum(player_cards)
    print(f"Your cards: {player_cards[0]}, {player_cards[1]}\nCurrent score: {player_score}")
    dealer_score = sum(dealer_cards)
    print(f"\nDealer's first card: {dealer_cards[0]}")


    main_flow()