# Step 1: Find valid moves for the first tile
# Step 2: Get a move from the user
# Step 3: If the move from the user is valid then move, othewise let him know that it is unvalid and get a new move from the user
# Step 4: Find valid moves for the next tile
# Step 5: Do step 2-4 until the user is in tile 3.1
# Step 6: Victory!

def print_valid_moves(position):
    '''Takes in the position and prints out the valid moves'''
    if position == 1.1 or position == 2.1:
        print('You can travel: (N)orth.')
    elif position == 1.2:
        print('You can travel: (N)orth or (E)ast or (S)outh.')
    elif position == 1.3:
        print('You can travel: (E)ast or (S)outh.')
    elif position == 2.2 or position == 3.3:
        print('You can travel: (S)outh or (W)est.')
    elif position == 2.3:
        print('You can travel: (E)ast or (W)est.')
    elif position == 3.2:
        print('You can travel: (N)orth or (S)outh.')

def direction_from_user():
    '''Gets a N, W, E or S from the user, (depending on where the user wants/can move) and returns it '''  
    direction = input('Direction: ')
    return direction

def is_move_valid(position, direction):
    '''Takes in the direction from user and the current position and checks if the direction is valid, and returns True or False''' 

    if direction == 'n' or direction == 'N':
        if position == 1.1 or position == 2.1 or position == 1.2 or position == 3.2:
            return True
    elif direction == 's' or direction == 'S':
        if position == 1.2 or position == 1.3 or position == 2.2 or position == 3.3 or position == 3.2:
            return True
    elif direction == 'e' or direction == 'E':
        if position == 1.2 or position == 1.3 or position == 2.3:
            return True
    elif direction == 'w' or direction == 'W':
        if position == 2.2 or position == 3.3 or position == 2.3:
            return True



def move(position, direction):
    '''Takes the current tile and move direction in and returns the new tile''' 
    if direction == "n" or direction == "N":
        position += 0.1
    elif direction == "s" or direction == "S":
        position -= 0.1
    elif direction == "e" or direction == "E":
        position += 1
    elif direction == "w" or direction == "W":
        position -= 1

    #we formatted the position so it only had 1 decimal place 
    position = float(("{:.1f}".format(position)))
    return position


def pull_lever_y_n(position, coins_from_lever):
    ''' '''
    if position == 1.2 or position == 2.2 or position == 2.3 or position == 3.2:
        
        pull_lever = input("Pull a lever (y/n): ")
        
        if pull_lever == "y" or pull_lever == "Y":
            coins_from_lever += 1
            print("You received 1 coin, your total is now {}.".format(coins_from_lever))
            return coins_from_lever

        else:
            return coins_from_lever
    
    else:
        return coins_from_lever




#main program starts here
start_position_float = 1.1
coins_from_lever = 0

position = start_position_float

print_valid_moves(position)


while position != 3.1:

    direction = direction_from_user()

    if is_move_valid(position, direction) == True:

        position = move(position, direction)

        coins_from_lever = pull_lever_y_n(position, coins_from_lever)

        print_valid_moves(position)

    else:
        print("Not a valid direction!")


else:
    print("Victory! Total coins {}.".format(coins_from_lever))
