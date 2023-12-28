def human(rolls, options, curtiles):
    """interfaces with human player"""
    print(f"your rolls are {rolls}, which sum to {sum(rolls)}")
    print(f"this means your options are {options}")
    while True:
        choice = [int(x) for x in input("please type in the tiles you would like to put down, seperated by a space:\n").split()]
        if choice in options:
            return choice

def fewestTiles(rolls, options, curtiles):
    """picks the option with the fewest tiles. Can 
    implement easily thanks to how choices are generated"""
    # print(options)
    return options[-1]


def mostTiles(rolls, options, curtiles):
    """picks the option with the most tiles. Can 
    implement easily thanks to how choices are generated"""
    # print(options)
    return options[0]

def fewestTilesMid(rolls, options, curtiles):
    """shortest len list but deviate towards middle numbers"""
    # print(options)
    shortest = min(len(op) for op in options)
    