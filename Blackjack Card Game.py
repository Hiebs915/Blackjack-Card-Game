import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

palying = True

#-----------------------------------------------------------------------------#

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

#-----------------------------------------------------------------------------#

class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Create the Card Object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

#-----------------------------------------------------------------------------#

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        # card passed in is from Deck.deal().  Deck.deal() is a single card(suit, rank)
        self.cards.append(card)
        self.value += value[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # IF TATAL VALUE > 21 AND I STILL HAVE AN ACE THEN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11.
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

#-----------------------------------------------------------------------------#

class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total = self.total + bet

    def lose_bet(self):
        self.total = self.total - bet

#-----------------------------------------------------------------------------#

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you don't have enough chips.  You have: {}".format(chips.total))
            else:
                break

#-----------------------------------------------------------------------------#

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

#-----------------------------------------------------------------------------#

def hit_or_stand(deck,hand):
    global palying
    while True:
        x = input("Hit or stand?  Enter h or s")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player stands, dealer's turn")
            playing = False
        else:
            print("Sorry, I did not understand that, please enter h or s")
            contine
        break

#-----------------------------------------------------------------------------#

def player_busts(player,dealer,chips):
    print("Player Busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player Wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Player Wins!  Dealer busted")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer Wins!")
    chips.lose_bet()

def push(player,dealer,chips):
    print('Dealer and player tie! PUSH')
