import random
import strats

def diceroll(numdice=2, numface=6):
    """returns a numdice long list of 
    dice rolls ranging from 1 to numface"""
    return [random.randint(1,numface) for _ in range(numdice)]

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

def makechoice(rolls, options, curtiles, strategy):
    """takes a set of tile choices with
     other info and returns one (int list)"""
    choice = strategy(rolls, options, curtiles)
    return choice


def game(player, tiles=range(1, 10), numdice=2 ,numface=6, prints=True):   #maybe optimise somehow with set
    curtiles = list(tiles)
    while True:
        rolls = diceroll(numdice, numface)
        options = get_legal_moves(curtiles, sum(rolls)) # maybe don't even need xsum for human players, just for robodogs

        if prints:
            print(f"rolled: {rolls}, total: {sum(rolls)}") #replace with render function
            print(f"remaining tiles are {curtiles}") #replace with render function

        if len(options) == 0:
            if prints:
                print(f"game over :( your score is {sum(curtiles)}")
            return sum(curtiles) # return score at end of game
        
        choice = makechoice(rolls, options, curtiles, player)
        
        if prints:
            print(f"you chose: {choice} !")

        for tile in choice:
            curtiles.remove(tile)


if __name__ == "__main__":
    game(strats.fewestTiles)
    print(get_legal_moves([1,2,3,4,5,6,7,8,9], 5))