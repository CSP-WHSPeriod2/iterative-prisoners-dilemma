####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random
team_name = 'BreadGetters' # Only 10 chars displayed.
strategy_name = 'Getting Bread'
strategy_description = 'gets bread'
n=-1
g=[0]
def alg_test(my_history,their_history,my_score,their_score):
    if(their_history[-1] == their_history[-2]):
        if(their_history[-1] == 'b'):
            return 'b'
        else:
            return 'c'
    elif(their_history[-1] == their_history[-3]):
        if(their_history[-1] == 'b'):
            return 'b'
        else:
            return 'c'
    elif(their_history[-1] == their_history[-4]):
        if(their_history[-1] == 'b'):
            return 'b'
        else:
            return 'c'
    elif(their_history[-1] == their_history[-5]):
        if(their_history[-1] == 'b'):
            return 'b'
        else:
            return 'c'
    elif(their_history[-1] == their_history[-6]):
        if(their_history[-1] == 'b'):
            return 'b'
        else:
            return 'c'
    elif(their_history[-1] == their_history[-7]):
        if(their_history[-1] == 'b'):
            return 'b'
        else:
            return 'c'
    elif(their_history[-1] == their_history[-8]):
        if(their_history[-1] == 'b'):
            return 'b'
        else:
            return 'c'
    elif(their_history[-1] == their_history[-9]):
        if(their_history[-1] == 'b'):
            return 'b'
        else:
            return 'c'
    elif(their_history[-1] == their_history[-10]):
        if(their_history[-1] == 'b'):
            return 'b'
        else:
            return 'c'
    
def ygolohcysp(my_history, their_history, my_score, their_score):
    if (their_history[-1] == 'b'):
        return 'c'
    else:
        return 'b'

def bodds(my_history, their_history, my_score, their_score):
    global n
    global g
    n+=1
    l=g[n]+1
    g=g+l
    if random.randint(1,100) in g:
        return 'b'
    else:
        return alg_test(my_history, their_history, my_score, their_score)
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if(len(my_history) <= 10):
        if(len(my_history == 0)):
            return 'b'
        return ygolohcysp(my_history, their_history, my_score, their_score)
    if(my_score >= their_score):
        return ygolohcysp(my_history, their_history, my_score, their_score) 
    elif(len(my_history)>=50):
        return bodds()
    else:
        return alg_test(my_history,their_history, my_score, their_score)
        
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'
    return 'c'