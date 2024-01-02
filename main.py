# i actually don't even think i need this lol idk
# people just be out here making files called main init
# gonna work on my superbot here
import simtools


def get_legal_moves(nums, roll):
    """returns a list of all combinations 
    from nums that sum to total"""
    def backtrack(start, target, path, result):
        if target < 0:
            return
        if target == 0 :
            result.append(path)
            return
        for i in range(start, len(nums)):
            backtrack(i+1, target - nums[i], path + [nums[i]], result)
    result = []
    backtrack(0, roll, [], result)
    return result


def optimalplay(tiles=range(1,10), numdice=2, numface=6):
    """returns a dict of all possible gamestates 
    & their average scores with optimal play"""
    gamestates = simtools.gen_gamestates(tiles)
    rollprobs = simtools.dice_roll_probs(numdice, numface)
    gamestate_scores = {}   #expected score with optimal play
    gamestate_scores[()] = 0
    for board in gamestates:
        score = bestavgscore(board, rollprobs, gamestate_scores) # calc avg score with best play
        gamestate_scores[board] = round(score,2)
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
                gamestates = get_new_gamestates(board, legal)  # board is a tuple
                                                   # get gamestates resulting from legal moves above then 
                for gamestate in gamestates:
                    poss_avg_scores_for_this_roll.append(bestavgscore(gamestate, rollprobs, cache))
                avg_score_for_board += min(poss_avg_scores_for_this_roll) * prob

    return avg_score_for_board


def get_new_gamestates(board, moves):
    """returns a list of the boardstates resulting
    from each move in lists acted upon board (refreshing in between)"""
    poss_new_boards = []
    for move in moves:
        new_board = list(board)
        for tile in move:
            new_board.remove(tile)
        poss_new_boards.append(tuple(new_board))
    return poss_new_boards



# print(get_new_gamestate((1,2,3,4), (1,2)))

# print(bestavgscore((1,2,3), {1:0.5, 2:0.5}, {}))


# gamestates = simtools.gen_gamestates(range(1,10))
# diceprobs2d6f = simtools.dice_roll_probs(2,6)
# print(diceprobs2d6f)
if __name__ == "__main__":
    print(optimalplay(tiles=range(1,10), numdice=2, numface=6)) 
#woohoo! (generates board that are impossible to reach in actual play due to starting from bottom up, but predictions are still sensible)