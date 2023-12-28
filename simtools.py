import math
import numpy as np
import game
import strats

def ntrials(n, game, player):
    """takes a game that returns an int.
    Runs n trials and returns player + summary stats in a dict."""
    scores = np.zeros(n)
    for i in range(n):
        scores[i] = game(player=player, prints=False)
    stats = {}
    stats["mean"] = np.mean(scores)
    stats["std"] = round(np.std(scores), 2)
    return player.__name__, stats

#std seems to be roughly equivalent between mostTiles & leastTiles, though the mean for leastTiles seems to be about 50% of that of mostTiles


print(ntrials(10000, game.game, strats.mostTiles))