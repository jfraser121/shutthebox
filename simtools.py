from collections import defaultdict
from itertools import product, combinations
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

# def get_legal_rolls

def ntrials(n, game, player):
    """takes a game that returns an int.
    Runs n trials and returns player + summary stats in a dict."""
    scores = np.zeros(n)
    for i in range(n):
        scores[i] = game(tiles=range(2,10), player=player, prints=False)
        # print("GAME OVER \n")
    stats = {}
    stats["mean"] = np.mean(scores)
    stats["std"] = round(np.std(scores), 2)
    return player.__name__, stats


def avgscore(boardstate, rollprobs):
    """return the average score acheieved
    from a given gamestate"""
    avg_score = 0 
    
def gen_gamestates(tiles):
    """generates a list of all possible gamestates 
    not incl 0. is a list of tuples"""
    gamestates = []
    for r in tiles:
    # Generate combinations of length r (board is an iterator)
        board = combinations(tiles, r)
        gamestates.extend(board)
    return gamestates



if __name__ == "__main__":
    # print(gen_gamestates(range(1,10)))
    # rollprobs_2d_6f = (dice_roll_probs(2,6))
    # print("\n\n")
    # print(rollprobs_2d_6f)
    # print(ntrials(10000, game.game, strats.mostTiles))
    print(ntrials(10000, game.game, strats.fewestTiles))
    # print(ntrials(10000, game.game, strats.fewestTiles))


