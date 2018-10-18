####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'team_IslandRoyale' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
def checker(their_history, my_history, my_score):
            if my_score >= -999:
                if their_history[-1] + their_history[-2] + their_history[-3] == 'cbc' or\
                their_history[-1] + their_history[-2] + their_history[-3] == 'ccb' or\
                their_history[-1] + their_history[-2] + their_history[-3] == 'bcc':
                    return 'c'
                elif their_history[-1] + their_history[-2] + their_history[-3]== 'bcb' or\
                their_history[-1] + their_history[-2] + their_history[-3] == 'cbb' or\
                their_history[-1] + their_history[-2] + their_history[-3] == 'bbc':
                    return 'b'
            elif my_score <= -1000:
                    return 'b'  
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(their_history)==0 or 1 or 2:
        return 'b'
    else:
        return checker(their_history, my_history, my_score)
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.