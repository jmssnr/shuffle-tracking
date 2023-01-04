import numpy as np
from scipy.stats import bernoulli
from .cards import Deck


def riffle_shuffle(deck: Deck) -> Deck:

    nL = np.random.binomial(52, 0.5)
    nR = 52 - nL

    L = deck[0:nL]
    R = deck[nL:52]
    j = 0
    k = 0

    shuffle = []

    for i in range(0, 52):
        c = bernoulli.rvs(float(nR) / (nL + nR), loc=0, size=1, random_state=None)
        if c == 0:
            shuffle.append(L[j])
            nL = nL - 1
            j = j + 1
        elif c == 1:
            shuffle.append(R[k])
            nR = nR - 1
            k = k + 1
    deck = shuffle

    return deck
