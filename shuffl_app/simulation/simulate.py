from .cards import Deck
from .shuffles import riffle_shuffle
from typing import List


def simulate_shuffles(n: int) -> List[Deck]:

    results = []

    for _ in range(0, n):
        deck = Deck()
        deck.cards = riffle_shuffle(deck.cards)
        results.append(deck)

    return results
