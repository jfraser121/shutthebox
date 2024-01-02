import random
# import strats
import main
import sys
print(sys.path)

def diceroll(numdice=2, numface=6):
    """returns a numdice long list of 
    dice rolls ranging from 1 to numface"""
    return [random.randint(1,numface) for _ in range(numdice)]


def makechoice(rolls, options, curtiles, strategy):
    """takes a set of tile choices with
     other info and returns one (int list)"""
    choice = strategy(rolls, options, curtiles)
    return choice


def game(player, tiles=range(1, 10), numdice=2 ,numface=6, prints=True):   #maybe optimise somehow with set
    curtiles = list(tiles)
    while True:
        rolls = diceroll(numdice, numface)
        options = main.get_legal_moves(curtiles, sum(rolls)) # maybe don't even need xsum for human players, just for robodogs

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


def coach(tiles=range(1,10), numdice=2, numface=6):
    current_board = list(tiles)
    optimal_play = main.optimalplay(tiles, numdice, numface)

    while True:
        rolls = diceroll(numdice, numface)
        options = main.get_legal_moves(current_board, sum(rolls))
        poss_boards = main.get_new_gamestates(current_board, options)

        if len(options) == 0:
            print(f"game over :( your score is {sum(current_board)}")

        best_option = []
        for move,board,score in zip(options,poss_boards,[optimal_play[board] for board in poss_boards]):
            if len(best_option)==0 or score < best_option[-1]:
                best_option = [move, board, score]

        print(f"the board currently looks like {current_board}, and you have rolled {rolls}, totalling {sum(rolls)}")
        print(f"this means your options are: {options}\n")
        
        move = [int(n) for n in input("make your choice! (seperate each tile with a space or i will break)\n").split()]

        wrong_count = 0
        while move != best_option[0]:
            wrong_count += 1
            if wrong_count < 2:
                print("that isn't the optimal move! try again :)")
            else:
                print(f"the optimal move is {best_option[0]}... Play it!")
            move = [int(n) for n in input("make your choice!\n").split()]
        print("\ngood choice. next roll!\n")
            
        for tile in move:
            current_board.remove(tile)

if __name__ == "__main__":
    # game(strats.fewestTiles)
    # print(get_legal_moves([1,2,3,4,5,6,7,8,9], 5))
    coach()