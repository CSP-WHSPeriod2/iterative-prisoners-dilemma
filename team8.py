####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team CoKayne' # Only 10 chars displayed.
strategy_name = 'CopyCat'
strategy_description = 'Finds the most used action and replicates it'

def find_most_common(their_history):
    for a in their_history:
        count_of_c = their_history.count('c')#Checking the amount of b's or c's in their history and copying the most common
        count_of_b = their_history.count('b')
        if count_of_c > count_of_b:
                return 'c'
        elif count_of_c == count_of_b:#If equal we return b
                return 'b'
        else:
                return 'b'
  
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    if len(my_history)==0: #starting move
        return 'c'
    elif len(their_history)<0:
        return(find_most_common)
