import random
import time

def display():
    print('***********************')
    print('       WELCOME         ')
    print(' RUSSIAN ROULETTE V2.0 ')
    # Using format strings for cleaner layout
    print(f'       |PLAY|LAY|      ')
    print('***********************')

def display_turn_prompt():
    print('***********************')
    print('       |SHOOT|LAY|     ')
    # .strip().title() cleans up accidental spaces from the user
    return input('Make your choice: ').strip().title()

def get_contributions(num_players):
    playerdata = {}
    total_pool = 0
    
    for i in range(1, num_players + 1):
        # NOTE: Added a try-except block to prevent crashes if the user types letters instead of numbers
        while True:
            try:
                bet = int(input(f'How much is Player {i} contributing: $'))
                break
            except ValueError:
                print("Please enter a valid number.")
                
        playerdata[i] = bet
        total_pool += bet
        
    return playerdata, total_pool

def play_game():
    display()
    choice = input('Are you ready? (Play/Lay): ').strip().title()
    
    if choice != 'Play':
        print('Maybe next time!')
        return

    # Error handling for number of players
    try:
        num_players = int(input('How many people are playing?: '))
    except ValueError:
        print("Invalid number. Exiting.")
        return

    # NOTE: We now return playerdata directly from the function instead of using a global variable
    player_data, total_money = get_contributions(num_players)
    print(f'\nTotal prize pool is: ${total_money}\n')

    print('LOADING THE CYLINDER...')
    time.sleep(1)
    
    # AMPLIFICATION: We simulate a real 6-chamber cylinder instead of a 50/50 chance.
    chamber = [1, 0, 0, 0, 0, 0] # 1 is the bullet, 0 is empty
    random.shuffle(chamber)

    print('GAME START!\n')

    # We loop as long as there are players left AND a bullet in the chamber
    while len(player_data) > 0 and 1 in chamber:
        
        # NOTE: We iterate over a LIST of the current active players. 
        # We can't iterate over a dictionary while deleting items from it.
        active_players = list(player_data.keys())
        
        for player_id in active_players:
            # If the bullet was fired by a previous player in this loop, stop the round
            if 1 not in chamber:
                break 

            print(f"\n--- Player {player_id}'s Turn ---")
            action = display_turn_prompt()

            if action == 'Shoot':
                print('Clocking......')
                time.sleep(1)
                print('You pull the trigger....')
                time.sleep(1)
                
                # Pop the next chamber (removes and returns the last item in the list)
                shot = chamber.pop() 

                if shot == 1:
                    print('💥 BANG! You Died!')
                    del player_data[player_id] # Player is removed safely
                else:
                    print('CLICK! No bullet.')
                    # Multiply their current money by 2 as a reward for surviving
                    player_data[player_id] *= 2 
            
            elif action == 'Lay':
                print("You passed your turn.")
                continue
            else:
                print("Invalid choice, you lose your turn!")

    # End of Game Results
    print('\n*** GAME OVER ***')
    print('SURVIVOR WALLETS:')
    if not player_data:
        print("No survivors.")
    else:
        # NOTE: Using .items() to properly unpack the dictionary
        for player, money in player_data.items():
            print(f"Player {player} walked away with ${money}")

if __name__ == '__main__':
    play_game()