from collections import defaultdict
from itertools import product
import math
import numpy as np
import game
import strats

def dice_roll_probs(num_dice, num_faces):
    """returns dict of roll totals and corresponding probabilities"""
    counts = defaultdict(float)
    total = pow(num_faces, num_dice)

    for dice_values in product(range(1, num_faces + 1), repeat=num_dice):
        sorted_values = sum(dice_values)
        counts[sorted_values] += round(1 / total, 3) # rounding means probs add up to 1.008 but such is life
    result = dict(counts)
    return result

rollprobs_2d_6f = (dice_roll_probs(2,6))

def get_legal_rolls

def ntrials(n, game, player):
    """takes a game that returns an int.
    Runs n trials and returns player + summary stats in a dict."""
    scores = np.zeros(n)
    for i in range(n):
        scores[i] = game(player=player, prints=False)
        # print("GAME OVER \n")
    stats = {}
    stats["mean"] = np.mean(scores)
    stats["std"] = round(np.std(scores), 2)
    return player.__name__, stats


def avgscore(boardstate, rollprobs):
    """calculates the average score acheieved
    from a given gamestate"""
    legal_rolls = get_legal_rolls(boardstate)
