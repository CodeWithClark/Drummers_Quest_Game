# Jordan Clark

import sys

def main_menu(): # Main menu function
    print("\nThe Drummer's Quest Adventure Game!".upper())   # Title
    print("Collect the 7 pieces of gear you need to perform your gig tonight and win the game.")   # How to win
    print("If you run into your ex, you will never make it to your gig and loose the game.")   # How to lose
    print('\nPossible Moves:')   # Possible directions
    print('\t"n": north, "s": south, "e": east, "w": west')
    print("\nGear:") # How to add gear
    print("\tSelect 'y' to add to your gear list.")
    print("\tSelect 'n' to decline.")
    print("\tIf you change your mind: type 'item' to view and collect available item.")
    #print('\nType "item" in the "Where to?" prompt to view and collect available item.')
    print('\nType "exit" in the "Where to?" prompt to quit at anytime.')   # Exit strategy
    print('='*75)

def status(rooms, current_room, inventory):
    print('-' * 75)  # Section display
    print('Gear list: ', inventory)  # Show inventory
    print('Location: ', current_room)
    possible_moves = rooms[current_room].keys()  # Connect moves to room dict.
    print('Possible moves: ', *possible_moves)  # Show possible moves
    print('-' * 75)  # Section display
    return


def get_item(current_room, rooms, inventory):   # Function for collecting gear.
    inventory.append(rooms[current_room]['item'])   # Add item to inventory
    del rooms[current_room]['item']   # Remove item from the room

def check_win():   # Win Function
    print('*' * 75)
    print('YOU WIN! Now go play those drums!!')
    print('  -^-_  _')
    print('  / [_][_]_:_')
    print(' /|  _||_  v')
    print('  | /    \ |')
    print(r'=/=\\____//=\=')
    print('*' * 75)
    play_again()

def lose(current_room):   # Lose Function
    print("\nOH NOOOOO! You've been spotted by your ex.")
    print()
    print(r'             ,      ,')
    print(r'            /(.-""-.)\\')
    print(r'        |\  \/      \/  /|')
    print(r'        | \ / =.  .= \ / |')
    print(r'        \( \   o\/o   / )/')
    print(r"         \_, '-/  \-' ,_/")
    print(r"           /   \__/   \\")
    print(r'           \ \__/\__/ /')
    print(r'         ___\ \|--|/ /___')
    print(r'       /`    \      /    `\\')
    print(r"      /       '----'       \\")
    print('\nYour ex is coming straight to you.')
    print('You will never make it to your gig now...')
    print('\nYOU LOSE.')
    play_again()

def play_again():    # Prompt user to play again
    user_input_again = input('\nTry again? (y or n)\n>>> ').lower()
    if user_input_again == 'y':
        game()
    elif user_input_again == 'n':
        print('Good-bye.')
        sys.exit()
    else:
        print("\nIt's an easy yes or no.\n") # Input validation
        play_again()

def game(): # Game Function
    # Map dictionary
    rooms = {
        'Home Sweet Home': {'n': 'North Shore', 's': 'South Shore', 'w': 'Brighton'},
        'North Shore': {'s': 'Home Sweet Home', 'e': 'Commonwealth', 'item': 'hardware'},
        'Commonwealth': {'s': 'Eastie', 'west': 'North Shore'},
        'Eastie': {'n': 'Commonwealth', 's': 'Cambridge', 'item': 'snare drum'},
        'Cambridge': {'n': 'Eastie', 'w': 'South Shore', 'item': 'drum accessories'},
        'South Shore': {'n': 'Home Sweet Home', 'e': 'Cambridge', 'w': 'Somerville', 'item': 'stickbag'},
        'Somerville': {'n': 'Brighton', 'e': 'South Shore', 'item': 'toms'},
        'Brighton': {'n': 'Quincy Market', 's': 'Somerville', 'e': 'Home Sweet Home', 'item': 'cymbals'},
        'Quincy Market': {'s': 'Brighton', 'item': 'kick drum'},
    }

    inventory = []   # Inventory List
    current_room = 'Home Sweet Home'   # Starting room
    main_menu()   # Show player main menu

    direction = ""   # Display current room with proper syntax
    while direction != 'exit':
        if current_room == 'Home Sweet Home':
            print("\nYou're {}.\n".format(current_room))
        elif current_room == 'North Shore':
            print("\nYou're in the {}.\n".format(current_room))
        elif current_room == 'South Shore':
            print("\nYou're in the {}.\n".format(current_room))
        else:
            print("\nYou're in {}.\n".format(current_room))

        if current_room != 'Commonwealth' and 'item' in rooms[current_room].keys():
            print('You see your {}!!'.format(rooms[current_room]['item']))   # Display item in current room

            # USER INPUT TO COLLECT ITEM
            collect_item = input('Do you want to collect your gear? (y or n) >> ').lower()
            if collect_item == 'y':
                get_item(current_room, rooms, inventory)   # Add item to gear list
                print('\nOne step closer!!\n')

                # WIN GAME
                if len(inventory) == 7:
                    check_win()

            elif collect_item == 'n':
                print('\nToo bad.\n')   # Allow user to decline
            else:
                print('\nNot sure what that means...\n')   # Input validation
                continue

        # LOSE GAME
        if current_room == 'Commonwealth':
            lose(current_room)

        # DISPLAY STATUS
        status(rooms, current_room, inventory)

        # USER INPUT TO MOVE
        direction = input('\nWhere to?\n>> ').lower()   # Get command from player
        if 'item' in rooms[current_room].keys() and direction == 'item':   # Loop if input is 'item'
            print('\nThis location has your',rooms[current_room]['item'],'.')
            continue

        if direction in rooms[current_room].keys():
            current_room = rooms[current_room][direction]   # Move between rooms process
        elif direction != 'exit' or not rooms:  # error message
            print("\nInvalid direction.\n")
            continue
    else:
        print('\nGood-bye.') # Exit game
        sys.exit()
        return

game()
