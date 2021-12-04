import random
import rolldice
from itertools import product

class Card:
    def __init__(self, value, suit):
        """values: 0-13 (1=Ace, 2-10=Numbers, 11=J, 12=Q, 13=K, 0=Joker)
           suits: hearts, diamonds, clover, spades
           Joker: red, black
        """
        self.value = value
        self.suit = suit

class Tarot:
    def __init__(self, arcana, value, suit):
        """values: 0-14 (1=Ace, 2-10=Numbers, 11=Page, 12=Queen, 13=Knight, 14=King)
           suits: wands, cups, swords, pentacles or None (if major arcana)
           arcana: minor or major
        """
        self.arcana = arcana
        if arcana == 'major':
            self.value = value
            self.suit = None
        else:
            self.value = value
            self.suit = suit

class Deck:
    """A class to represent a base deck of cards, with methods for shuffling and drawing.
    """
    def __init__(self):
        self.deck = []  # draw pile
        self.draw = []  # draw
        # TODO: add a game table pile
        self.discard = []  # discard pile

    def shuffle(self, what='all'):
        if what == 'all':  # Shuffle back all cards
            self.deck = [self.deck, self.discard, self.hand]
        elif what == 'discard':  # Shuffle back discard pile
            self.deck = [self.deck, self.discard]
        elif what == 'hand':  # Shuffle back your hand
            self.deck = [self.deck, self.hand]
        random.shuffle(self.deck)  # else, only shuffle draw pile

    def draw(self, n=1):
        for i in range(n):
            self.hand.append(self.deck.pop())


class FrenchDeck(Deck):
    """A class to represent a french cards deck.
    """
    def __init__(self, joker=True):
        super(FrenchDeck, self).__init__()
        self.joker = joker
        self.new_deck()

    def new_deck(self):
        self.deck = []
        self.draw = []
        self.discard = []
        if self.joker:
            self.deck.append(Card(0, 'red'))  # red Joker
            self.deck.append(Card(0, 'black'))  # black Joker
        for i,j in product(range(1,14), ('hearts', 'diamonds', 'clubs', 'spades')):
            self.deck.append(Card(i, j))


class TarotDeck(Deck):
    """A class to represent a tarots deck.
    """
    def __init__(self):
        super(TarotDeck, self).__init__()
        self.new_deck()
        self.arcanaNames = ['The Fool','The Magician','The High Priestess','The Empress','The Emperor',
                            'The Hierophant','The Lovers','The Chariot','Strength','The Hermit',
                            'Wheel of Fortune','Justice','The Hanged Man','Death','Temperance',
                            'The Devil','The Tower','The Star','The Moon','The Sun','Judgement',
                            'The World']
    def new_deck(self):
        self.deck = []
        self.draw = []
        self.discard = []
        # minor arcana
        for i,j in product(range(1,15), ('wands', 'diamonds', 'swords', 'pentacles')):
            self.deck.append(Tarot('minor',i , j))
        # major arcana
        for i in range(0,22):
            self.deck.append(Tarot('major', i, None))
