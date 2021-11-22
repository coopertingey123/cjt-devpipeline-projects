import random

class GenericCard:
   def __init__(self, rank, suit):
      self.rank = rank
      self.suit = suit

   def __str__(self):
      return f'{self.rank}{self.suit}'

    # THIS CLASS TAKES IN A SUIT AND RANK FOR A CARD AND, WHEN CALLED, PRINTS THE RANK + SUIT

# card = GenericCard("Ace", "Spades")
# print(card)

class PlayingCard(GenericCard):

   names_to_symbols = {
      'Clubs': '♣',
      'Spades': '♠',
      'Diamonds': '♦',
      'Hearts': '♥'
   }

   def get_color(self):
      if self.suit in ['Clubs', 'Spades']:
         return 'black'
      return 'red'
   
   def __str__(self):
      return f'{self.rank}{PlayingCard.names_to_symbols[self.suit]}'

    # THIS CLASS CHANGES THE SUIT TO A SYMBOL, THATS IT!



# card = PlayingCard("Ace", "Spades")
# print(card)

class UnoCard(GenericCard):
   ranks_to_symbols = {
      'Skip': '⊘',
      'Reverse': '⤾',
      'Draw 2': '+2',
      'Wild': 'ω',
      'Wild Draw 4': 'ω+4'
   }
   def __str__(self):
      suit = self.suit[:1].lower()
      if suit == 'w':
         suit = ' '
      rank = self.rank
      if not rank.isnumeric():
         rank = UnoCard.ranks_to_symbols[self.rank]
      return f'{suit}{rank}'

    # THIS CLASS TURNS THE SUIT TO A LOWERCASE AND FIRST LETTER OF COLOR, AND  CONVERTS THE RANK TO A SYMBOL

# uno = UnoCard("Skip", "blue")
# print(uno)


class DeckOfCards:
   def __init__(self, cards=[]):
      self.cards = cards
    #   INITIALIZES CLASS AND IF CARDS ARE PASSED IN, THEY BECOME self.cards
   
   def __str__(self):
      return ', '.join([str(card) for card in self.cards])
    #   CONVERTS THE LIST OF CARDS TO A LIST OF CARDS

   def shuffle(self):
      number_of_shuffles = 100

      for i in range(number_of_shuffles):
         idx_1 = random.randint(0, len(self.cards) - 1)
         idx_2 = idx_1
         while idx_1 == idx_2:
            idx_2 = random.randint(0, len(self.cards) - 1)

         self.cards[idx_1], self.cards[idx_2] = self.cards[idx_2], self.cards[idx_1]
    # SHUFFLES WHATEVER CARDS ARE IN THE SELF.CARDS 

   def draw_card(self):
      return self.cards.pop()
    #   RETURNS A CARD FROM THE LIST OF CARDS
     
     
   def draw_cards(self, num=1):
      cards = []
      for _ in range(num):
         if len(self.cards) > 0:
            cards.append(self.draw_card())
      return cards
    # RETURNS A LIST OF HOWEVER LONG YOU WANT TO BE YOUR HAND OF CARDS (ex. input = 5 returns a hand of 5 cards from a shuffled deck)

   def draw_hand(self, num=1):
      return Hand(self.draw_cards(num))

   def is_empty(self):
      return len(self.cards) == 0

class DeckOfPlayingCards(DeckOfCards):
   def __init__(self):
      cards = []
      for suit in ['Spades', 'Diamonds', 'Hearts', 'Clubs']:
         for rank in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
            cards.append(PlayingCard(rank, suit))
      super().__init__(cards)

class DeckOfGoFishCards(DeckOfCards):
    def __init__(self):
        cards = []
        suits = ["shark", "whale", "clownfish", "eel", "starfish", "pufferfish", "seaturtle", "octopus", "swordfish", "barracuda"]
        rank = 1
        for suit in suits:
            cards.append(suit) * 4
        super().__init__(cards)
    
    

class DeckOfUnoCards(DeckOfCards):
   def __init__(self):
      colored_ranks = [
         '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9'
      ] + ['Skip']*2 + ['Draw 2']*2 + ['Reverse']*2
      wild_ranks = ['Wild'] * 4 + ['Wild Draw 4'] * 4
      
      cards = []
      for suit in ['Blue', 'Green', 'Red', 'Yellow']:
         for rank in colored_ranks:
            cards.append(UnoCard(rank, suit))
      for wild in wild_ranks:
         cards.append(UnoCard('Wild', wild))

      super().__init__(cards)


class Hand(DeckOfCards):
   pass

class UnoCard(GenericCard):
   ranks_to_symbols = {
      'Skip': '⊘',
      'Reverse': '⤾',
      'Draw 2': '+2',
      'Wild': 'ω',
      'Wild Draw 4': 'ω+4'
   }
   def __str__(self):
      suit = self.suit[:1].lower()
      if suit == 'w':
         suit = ' '
      rank = self.rank
      if not rank.isnumeric():
         rank = UnoCard.ranks_to_symbols[self.rank]
      return f'{suit}{rank}'

class GoFishCard(DeckOfCards):
    

    def __init__(self):
        cards = []
        suits = ["shark", "whale", "clownfish", "eel", "starfish", "pufferfish", "seaturtle", "octopus", "swordfish", "barracuda"]
        for suit in suits:
            cards.append(suit)
            cards.append(suit)
            cards.append(suit)
            cards.append(suit)
        self.cards = cards
    def show(self):
        return cards

cards = GoFishCard()

print(cards.show())
        


