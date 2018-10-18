####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The name the team gives to itself' 
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'When history is before 90, betray if other team betrays, else collude. After if score is still 0, poke.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history) <= 2:
        return 'c'
    elif len(my_history) < 90:
        if 'b' in their_history:
            return 'b'
        if my_history[-1] == 'c' and their_history[-2] == 'b':
            return 'b'
    if my_score == 0:
        if len(my_history) >= 90 and len(my_history) < 93:
            return 'b'
        elif len(my_history) >= 93 and len(my_history) < 96:
            return 'c'
        elif len(my_history) >= 96 and len(my_history) < 99:
            return 'b'
    elif len(my_history) >= 99:
        if my_history[95] == 'c' and their_history[95] == 'b':
            return 'b'
        elif my_score > their_score:
            return 'b'
    else:
        return 'b'
        
        

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
