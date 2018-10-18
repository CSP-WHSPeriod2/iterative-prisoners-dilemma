import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Exposed' # Only 10 chars displayed.
strategy_name = 'If neccessary'
strategy_description = 'How does this strategy decide?'

retaliation = ['b', 'b', 'c', 'c', 'b']
always_betray = ['b', 'b','b','b','b']
always_collude = ['c', 'c', 'c', 'c', 'c']
og_pattern = ['b','b','c','c','b']
strategies = [retaliation, always_betray, always_collude, og_pattern]
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history)==0:
        return 'b'
    if len(my_history)==1:
        return 'b'
    if len(my_history)==2:
        return 'c'
    if len(my_history)==3:
        return 'c'
    if len(my_history)==4:
        return 'b'
    if their_history == ['c', 'b', 'b', 'c', 'c']:
        if(len(my_history)%5==1):
            return retaliation[0]
        if(len(my_history)%5==2):
            return retaliation[1]
        if(len(my_history)%5==3):
            return retaliation[2]
        if(len(my_history)%5==4):
            return retaliation[3]
        if(len(my_history)%5==0):
            return retaliation[4]
    if their_history == ['c', 'c', 'c', 'c', 'c']:
        return 'b'
    if their_history == ['b', 'b', 'b', 'b', 'b']:
        return 'c'
    else:
        strat = random.choice(strategies)
        if strat == retaliation:
            if(len(my_history)%5==1):
                return retaliation[0]
            if(len(my_history)%5==2):
                return retaliation[1]
            if(len(my_history)%5==3):
                return retaliation[2]
            if(len(my_history)%5==4):
                return retaliation[3]
            if(len(my_history)%5==0):
                return retaliation[4]
        elif strat == always_betray: 
            return 'b'
        elif strat == always_collude: 
            return 'c'
        else: 
            if(len(my_history)%5==1):
                return og_pattern[0]
            if(len(my_history)%5==2):
                return og_pattern[1]
            if(len(my_history)%5==3):
                return og_pattern[2]
            if(len(my_history)%5==4):
                return og_pattern[3]
            if(len(my_history)%5==0):
                return og_pattern[4]
        
        

        
    

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'     