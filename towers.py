'''
A simple Tower Blaster game
'''

# import the random module
import random

def setup_bricks():
    """This function creates a main pile of 60 bricks from 1-60 and a discard pile of 0 bricks."""
    main_pile = list(range(1, 61))
    discard = []
    return (main_pile, discard)


def shuffle_bricks(bricks):
    """This function shuffles the bricks."""
    random.shuffle(bricks)


def check_bricks(main_pile, discard):
    """Check if there are any cards left in the given main pile of bricks."""
    if len(main_pile) == 0:
        discard = shuffle(discard)
        main_pile.append(discard)


def check_tower_blaster(tower):
    """This function determines if stability has been achieved given a tower."""
    # return True for stability and otherwise return False
    if sorted(tower) == tower:
        return True
    else:
        return False


def get_top_brick(brick_pile):
    """This function removes and returns the top brick from any given pile of bricks."""
    top_brick = brick_pile.pop(0)
    # return the removed top brick
    return top_brick


def deal_initial_bricks(main_pile):
    """This function deals two sets of 10 bricks each, from the given main_pile at the state of the game."""
    player_tower = []
    computer_tower = []
    # deal with 10 bricks
    for i in range(10):
        computer_tower.insert(0, get_top_brick(main_pile))
        player_tower.insert(0, get_top_brick(main_pile))

    return (computer_tower, player_tower)


def add_brick_to_discard(brick, discard):
    """Add the given brick to the top of the given discard pile."""
    discard.insert(0, brick)


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    """Find the given brick to be replaced in the given tower and replace it with the given brick"""
    # first line checks if the given brick to be replaced is truely a brick in the given tower
    if brick_to_be_replaced in tower:
        # get the index for the brick to be replaced in the tower
        index = tower.index(brick_to_be_replaced)
        # remove the brick to be replaced in the tower
        tower.pop(index)
        # the given brick to be replaced gets put on top of the given discard pile
        add_brick_to_discard(brick_to_be_replaced, discard)
        # the given new brick is put to the tower
        tower.insert(index, new_brick)
        return True

    else:
        return False


def computer_play(tower, main_pile, discard):
    """This function defines the computer's strategy."""

    # check if main_pile is empty before getting to the computer's turn
    check_bricks(main_pile, discard)

    # it's computer's turn!
    print("COMPUTER'S TURN")

    # evaluate the top brick on the discard pile

    # if the top brick on the discard pile is greater than 50, replace it with the bottom brick
    if discard[0] >= 50:
        print("The computer picked", discard[0], "from the discard pile")
        print("The computer replaced a brick")
        # add the given brick to the top of the given discard pile
        add_brick_to_discard(tower[9], discard)
        # take out the bottom brick from the tower
        tower.pop(9)
        # move the original top brick from the discard pile to the tower
        tower.insert(9, discard[1])
        discard.pop(1)


    elif discard[0] >= 40 and discard[0] < 50:
        print("The computer picked", discard[0], "from the discard pile")
        print("The computer replaced a brick")
        # add the given brick to the top of the given discard pile
        add_brick_to_discard(tower[8], discard)
        # take out the second brick from the bottom of the tower
        tower.pop(8)
        # move the original top brick from the discard pile to the tower
        tower.insert(8, discard[1])
        discard.pop(1)

    elif discard[0] >= 10 and discard[0] < 15:
        print("The computer picked", discard[0], "from the discard pile")
        print("The computer replaced a brick")
        # add the given brick to the top of the given discard pile
        add_brick_to_discard(tower[1], discard)
        # take out the second brick from the top of the tower
        tower.pop(1)
        # move the original top brick from the discard pile to the tower
        tower.insert(1, discard[1])
        discard.pop(1)

    elif discard[0] >= 0 and discard[0] < 10:
        print("The computer picked", discard[0], "from the discard pile")
        print("The computer replaced a brick")
        # add the given brick to the top of the given discard pile
        add_brick_to_discard(tower[0], discard)
        # take out the top brick from the tower
        tower.pop(0)
        # move the original top brick from the discard pile to the tower
        tower.insert(0, discard[1])
        discard.pop(1)

    # make the computer deterministic for picking from the main pile: always reject it
    else:
        print("The computer picked", discard[0], "from the discard pile")
        print("The computer did not replace a brick")


    return (tower, main_pile, discard)


def user_play(tower, main_pile, discard):
    """this function shows the prompt for the user to play.
    It will asks the user which pile to choose, and whether the user wants the brick to be replaced.
    It also checks if the stability has been achieved.
    """

    # check if main_pile is empty before getting to the computer's turn
    check_bricks(main_pile, discard)

    # it's the player's turn!
    print("NOW IT'S YOUR TURN!")
    print("Your Tower:", tower)
    print('The top brick on the discard pile is', discard[0])

    # ask the user to choose which pile to pick
    user_choice = input('Type D to take the discard brick, M for a mystery brick and H for help.')

    while user_choice not in ['D', 'd', 'M', 'm', 'H', 'h']:
        print('Invalid entry. Please type D, M or H.')
        user_choice = input('Type D to take the discard brick, M for a mystery brick and H for help.')

    if user_choice == 'D' or user_choice == 'd':
        print('You picked the discard brick.')

        replace = int(input('Where do you want to place this brick? Type a brick number to replace in your tower: '))

        rep_brick = find_and_replace(discard[0], replace, tower, discard)

        # repeat until user put valid input
        while rep_brick == False:
            print("No brick found in your tower. Type a brick number again.")
            replace = int(input('Where do you want to place this brick? Type a brick number to replace in your tower: '))
            rep_brick = find_and_replace(discard[0], replace, tower, discard)

        find_and_replace(discard[0], replace, tower, discard)
        discard.pop(1)

    if user_choice == 'M' or user_choice == 'm':
        print('YYou picked', main_pile[0], "from main pile")
        myster = input("Do you want to use this brick. Type Y or N to skip turn")

        while myster not in ['Y', 'y', 'N', 'n']:
            print('Invalid entry. Please type Y, y, N or n.')
            myster = input("Do you want to use this brick. Type Y or N to skip turn")

        if myster == 'Y' or myster == 'y':
            replace = int(input('Where do you want to place this brick? Type a brick number: '))
            find_and_replace(discard[0], replace, tower, discard)
            main_pile.pop(0)
        if myster == 'N' or myster == 'n':
            print("You skip this turn")
            discard.insert(0, main_pile[0])
            main_pile.pop(0)

    if user_choice == 'H' or user_choice == 'h':
        print('A Tower Blaster game starts with a main pile of 60 bricks, each numbered from 1 to 60. Think of the numbers on the bricks as the width of the bricks. The objective is to be the first player to arrange 10 bricks in your own tower from lowest to highest (from the top down).')

    return (tower, main_pile, discard)


def main():

    status = True
    userinput = input("Do you want to start the Tower Blaster game?")
    if userinput[0] == 'y' or userinput[0] == 'Y':
        status = False

    # setup_bricks to get a tuple of two lists.
    main_pile, discard = setup_bricks()

    while status == False:
        # shuffle the bricks in the main pile
        shuffle_bricks(main_pile)

        # deal the first 10 cards to computer and user, respectively
        computer_tower, player_tower = deal_initial_bricks(main_pile)

        print('Comupter tower is:', computer_tower)
        print('Your tower is:', player_tower)

        # call the function remove and return the top brick from the main pile
        # add the top brick from the main pile to the top of the given discard pile.
        main_top = get_top_brick(main_pile)
        add_brick_to_discard(main_top, discard)

        print("discard pile:", discard)

        stability = False
        while stability == False:
            print('')
            computer_tower, main_pile, discard = computer_play(computer_tower, main_pile, discard)
            print('Computer tower', computer_tower)

            print('')

            user_tower, main_pile, discard = user_play(player_tower, main_pile, discard)
            print("Your tower:", user_tower)
            print("discard pile: ", discard)

            stability = check_tower_blaster(computer_tower) or check_tower_blaster(user_tower)

        if check_tower_blaster(computer_tower) == True:
            print('The computer wins!')

        elif check_tower_blaster(user_tower) == True:
            print('You win!')

        status = True


if __name__ == '__main__':
    main()
