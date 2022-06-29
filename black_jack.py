class Player:
    def __init__(self, name):
        self.money = 1000
        self.name = name
        self.hand = []
    def hit(self, deck):
        # append a card from the top of the deck to the hand
        self.hand.append(deck.pop())
    def show_hand(self):
        # print the cards in the hand
        for card in self.hand:
            print(card)
    def get_value(self):
        # return the value of the hand
        value = 0
        for card in self.hand:
            value += card["value"]
        return value
    def clear_hand(self):
        # clear the hand
        self.hand = []
    def bet(self, amount):
        # subtract the amount from the money
        self.money -= amount
    def win(self, amount):
        # add the amount to the money
        self.money += amount
        print("won round", amount)
    def lose(self, amount):
        # subtract the amount from the money
        self.money -= amount
        print("lost round", amount)
    def push(self):
        # do nothing
        pass

def construct_card(name, suit, value):
    # create a card dictionary
    card = {
        "name": name,
        "suit": suit,
        "value": value
    }
    return card

def construct_deck():
    # create a deck of cards
    deck = []
    for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
        for value in range(2, 11):
            deck.append(construct_card(str(value), suit, value))
        for name in ["Jack", "Queen", "King"]:
            deck.append(construct_card(name, suit, 10))
        deck.append(construct_card("Ace", suit, 11))
    return deck

def randomize_deck(deck):
    # shuffle the deck
    import random
    random.shuffle(deck)
    return deck

class Dealer:
    def __init__(self):
        self.hand = []
    def hit(self, deck):
        # append a card from the top of the deck to the hand
        if self.get_value() < 17: 
            self.hand.append(deck.pop())
    def show_hand(self):
        # print the cards in the hand
        print(self.hand[0])
    def get_value(self):
        # return the value of the hand
        value = 0
        for card in self.hand:
            value += card["value"]
        return value
    def clear_hand(self):
        # clear the hand
        self.hand = []
    def push(self):
        # do nothing
        pass

def game():
    # give player name from input
    name = input("your name here : ")
    player = Player(name)
    dealer = Dealer()
    deck = construct_deck()
    randomize_deck(deck)
    while True:
        if player.money == 0:
            print("you are out of money")
            break
        play_round(player,dealer,deck)

def play_round(player:Player,dealer:Dealer,deck):
    # play a round of black jack
    bet_amount = 0
    while True:
        bet_amount = int(input(f"bet amount must be < {player.money}: "))
        if bet_amount > player.money:
            print("not enough money")
        else:
            break
    player.bet(bet_amount)
    randomize_deck(deck)
    play_turn(player,dealer,deck,bet_amount)
    

def play_turn(player:Player,dealer:Dealer,deck ,bet_amount):
    # play a turn of black jack
    dealer.hit(deck)
    dealer.show_hand()
    player.hit(deck)
    player.show_hand()
    
    player_value = player.get_value()
    if player_value > 21:
        player.lose(bet_amount)
        print("bust")
        return
    while True:
        choice = input("hit or stay: ")
        if choice == "hit":
            player.hit(deck)
            player.show_hand()
            player_value = player.get_value()
            if player_value > 21:
                player.lose(bet_amount)
                print("bust")
                return
        elif choice == "stay":
            break
        else:
            print("invalid choice")
    
    dealer_value = dealer.get_value()
    if dealer_value > 21:
        player.win(bet_amount)
        print("dealer bust")
        return
    while True:
        if dealer_value < 17:
            dealer.hit(deck)
            dealer_value = dealer.get_value()
        else:
            break
    if player_value > dealer_value:
        player.win(bet_amount)
        print("player wins")
    elif player_value < dealer_value:
        player.lose(bet_amount)
        print("dealer wins")
    else:
        player.push()
        print("push")
    player.clear_hand()
    dealer.clear_hand()

