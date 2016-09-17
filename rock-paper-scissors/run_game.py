# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message
# of congratulations to the winner, and ask if the players want to start a new game)
#
# Rules:
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock

# check game rules and calculate results
def game_rules(play1Input, play2Input):
    if play1Input == play2Input:
        return 0
    elif play1Input == 'paper' and play2Input == 'scissors':
        return play2Input
    elif play1Input == 'scissors' and play2Input == 'rock':
        return play2Input
    elif play1Input == 'rock' and play2Input == 'paper':
        return play2Input
    else:
        return play1Input

# Check user inputs
def start_game():
    # Player 1: asks input again if entered anything other than rock, paper, scissors
    while True:
        player1 = raw_input('Player 1, You choose rock, paper or scissors?: ')
        if player1 not in ['rock', 'paper', 'scissors']:
            print "Invalid input. Please try again."
            continue
        break
        
    # Player 2: asks input again if entered anything other than rock, paper, scissors
    while True:
        player2 = raw_input('Player 2, You choose rock, paper or scissors?: ')
        if player2 not in ['rock', 'paper', 'scissors']:
            print "Invalid input. Please try again."
            continue
        break
        
    return game_rules(player1, player2)

# Execute game and declare result
while True:
    usr_command = raw_input('Shall we start a new Game? {Y/N]').lower()
    
    # should not type anything other than y OR n, else display error
    if usr_command not in ['y', 'n']:
        print "Invalid input. Please try again."
        continue
    
    if usr_command.lower() == 'n':
        break
    else:
        ret = start_game()
        
        if ret == 0:
            print "It's a tie"
        else:
            print "Congratulations!", ret, "wins."