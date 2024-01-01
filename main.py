# i actually don't even think i need this lol idk
# people just be out here making files called main init
# gonna work on my superbot here
from game import get_legal_moves
import simtools


def optimalplay(boardstates, rollprobs):
    """returns a dict of all possible gamestates 
    & their average scores with optimal play"""
    gamestate_scores = {}   #expected score with optimal play
    gamestate_scores[()] = 0
    for board in boardstates:
        score = bestavgscore(board, rollprobs, gamestate_scores) # calc avg score with best play
        gamestate_scores[board] = score
    return gamestate_scores


def bestavgscore(board, rollprobs, cache):
    if board in cache:
        return cache[board] # (score for that board)
    else:
        avg_score_for_board = 0
        for roll, prob in rollprobs.items():               #       for each roll, add board * prob to score if no legal moves,
                                                           # else find score of best legal move & add that * prob to score 
            legal = get_legal_moves(board, roll)             # after this is done for all rolls, board's avg score is calculated.
            if len(legal)==0:
                avg_score_for_board += sum(board) * prob
            else:
                poss_avg_scores_for_this_roll = []
                gamestates = []
                for move in legal:
                    gamestates.append(get_new_gamestate(board, move))  # board is a tuple
                                                   # get gamestates resulting from legal moves above then 
                for gamestate in gamestates:
                    poss_avg_scores_for_this_roll.append(bestavgscore(gamestate, rollprobs, cache))
                avg_score_for_board += min(poss_avg_scores_for_this_roll) * prob

    return avg_score_for_board


def get_new_gamestate(board, move):
    """takes board:tuple and legal moves:list and returns a 
    list of board states (tuples) after legal moves"""
    new_board = list(board)
    for tile in move:
        new_board.remove(tile)
    return tuple(new_board)



# print(get_new_gamestate((1,2,3,4), (1,2)))

# print(bestavgscore((1,2,3), {1:0.5, 2:0.5}, {}))


gamestates = simtools.gen_gamestates(range(1,10))
diceprobs2d6f = simtools.dice_roll_probs(2,6)
# print(diceprobs2d6f)

print(optimalplay(gamestates, diceprobs2d6f)) 
#woohoo! (generates board that are impossible to reach in actual play due to starting from bottom up, but predictions are still sensible)