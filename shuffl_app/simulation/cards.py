from dash_iconify import DashIconify
import dash_mantine_components as dmc

SUITS = ["hearts", "clubs", "spades", "diamonds"]

RANKS = ["ace"] + [str(rank) for rank in range(2, 11)] + ["jack", "queen", "king"]


class Card:
    def __init__(self, value: str, suit: str, pos: int = None):
        self.value = value
        self.suit = suit
        self.pos = pos

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, _value: str):
        if _value not in RANKS:
            raise ValueError(f"Value '{_value}' not in {RANKS}")
        self._value = _value

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, _suit: str):
        if _suit not in SUITS:
            raise ValueError(f"Suit '{_suit}' not in {SUITS}")
        self._suit = _suit

    @property
    def id(self):
        return self.value + self.suit

    def show(self):
        return dmc.Avatar(
            variant="outline",
            alt=f"{self.value} of {self.suit}",
            children=DashIconify(
                width=400,
                color="violet",
                icon=f"game-icons:card-{self.value}-{self.suit}",
            ),
        )

    def __repr__(self):
        return self.id


class Deck:
    def __init__(self):

        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]

    def reveal(self):
        cards_list = [card.show() for card in self.cards]

        groups = [cards_list[x : x + 13] for x in range(0, len(cards_list), 13)]
        return dmc.AvatarGroup(
            children=dmc.Stack(children=[dmc.Group(group) for group in groups]),
            spacing=30,
        )
