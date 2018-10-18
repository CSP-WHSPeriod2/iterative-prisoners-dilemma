####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The Sinkers' # Only 10 chars displayed.
strategy_name = "You're going down"
strategy_description = 'To cooperate unless they betray us. Once they betray 20 times or we are down 5000 point, \
we betray the rest of the game.'
    
def move(my_history, their_history, my_score, their_score, collectiveScore):
    numberOfBetrays = 0
    if(len(my_history) == 0):
        return 'c'
    else:
        if(their_history[-1] == 'b'):
            numberOfBetrays += 1
            return 'b'
        elif (their_history[-1] == 'c'):
            return 'c'
        elif (numberOfBetrays == 20 or my_score == -5000):
            return 'b'
    print (collectiveScore)

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    

def collectiveScore(my_history, their_history, my_score, their_score):
    myScore = 0
    theirScore = 0
    if (my_history[0] == 'c' and their_history[0] == 'c'):
        myScore += 0
        theirScore += 0
    elif (my_history[0] == 'c' and their_history[0] == 'b'):
        myScore += -500
        theirScore += 100
    elif (my_history[0] == 'b' and their_history[0] == 'c'):
        myScore += 100
        theirScore = -500
    else:
        myScore += -250
        theirScore += -250
    return myScore + theirScore