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
