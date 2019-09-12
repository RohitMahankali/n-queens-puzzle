import random
import matplotlib
import numpy

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
BFS add to queue 
'''

mainQ = []

def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    global mainQ
    if initialize:
        mainQ = [(node_id, parent_node_id)]
    else:
        mainQ.append((node_id, parent_node_id))
    
    return mainQ

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    # Your code here
    if mainQ:
        return False
    return True

'''
BFS pop from queue
'''
def pop_front_BFS():
    # Your code here
    global mainQ
    (node_id, parent_node_id) = mainQ.pop(0)
    return (node_id, parent_node_id)

'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    global mainQ
    if initialize:
        mainQ = [(node_id, parent_node_id)]
    else:
        mainQ.append((node_id, parent_node_id))
    
    return mainQ

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    # Your code here
    if mainQ:
        return False
    return True
'''
DFS pop from queue
'''
def pop_front_DFS():
    global mainQ
    (node_id, parent_node_id) = mainQ.pop()
    return (node_id, parent_node_id)

'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    global mainQ
    if initialize:
        mainQ = [(node_id, parent_node_id, cost)]
    else:
        mainQ.append((node_id, parent_node_id, cost))
    
    mainQ.sort(key=lambda tup: tup[2])
    return mainQ

'''
UC add to queue 
'''
def is_queue_empty_UC():
    if mainQ:
        return False
    return True

'''
UC pop from queue
'''
def pop_front_UC():
    global mainQ
    (node_id, parent_node_id, cost) = mainQ.pop(0)
    return (node_id, parent_node_id)

'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    global mainQ
    if initialize:
        mainQ = [(node_id, parent_node_id, cost)]
    else:
        mainQ.append((node_id, parent_node_id, cost))
    
    mainQ.sort(key=lambda tup: tup[2])
    return mainQ

'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    if mainQ:
        return False
    return True

'''
A* pop from queue
'''
def pop_front_ASTAR():
    global mainQ
    (node_id, parent_node_id, cost) = mainQ.pop(0)
    return (node_id, parent_node_id)


''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
Compute a random state 
'''
def get_random_state(n):
    state = []
    # Your code here
    
    for i in range (n):
   	 state.append(random.randint(1,n)) 
	# print str(state[i])+" ",
       
    return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):#We are assuming that state is a populated list of n elements
    number_attacking_pairs = 0
    # Your code here
    if state is None:
    	n = 0
    else:
        n = len(state)
    for i in range (n-1):
    	for j in range(i+1,n):
        	#Horizontal checks
        	if (state[i] == state[j]):
			number_attacking_pairs+=1
		#Diagonal checks
		if (state[i] == (state[j]+(j-i)) or state[i] == (state[j] - (j-i))):
			number_attacking_pairs+=1
   # print "attacking pairs: " + str(number_attacking_pairs)
    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
    
	
		
'''
def hill_desending_n_queens(state, comp_att_pairs):
    final_state = []
    # Your code her
    n = len(state)
    minCost = comp_att_pairs(state)
    while(minCost > A(state,comp_att_pairs)):
         state = B(state,comp_att_pairs)[:]
	 minCost = comp_att_pairs(state)
    final_state = state
    return final_state 	 

	 minCost = comp_att_pairs(state)
         print "minCost is: "+str(minCost),
    final_state = state
    for k in final_state:
         print k,
    return final_state 
Hill-climing algorithm for n queens with restart
'''
def make_neighbors(state):
    list = []
    neighbors = state[:]
    n = len(state)
    for i in range(n):
    	for j in range(1,n+1):
		neighbors[i] = j
		list.append(neighbors[:])
		neighbors[i] = state[i]
    neighbors = state
    return list

def cheapest_climbing(state,comp_att_pairs):
    list = make_neighbors(state)
    currCost = comp_att_pairs(state)
    index = -1
    n = len(list)
    for k in range(n):
    	if (currCost > comp_att_pairs(list[k])):
		index = k
		currCost = comp_att_pairs(list[k])
    return list[index]
    
def hill_desending_n_queens(state,comp_att_pairs):
    final_state = []
#    best = cheapest_climbing(state,comp_att_pairs)
    while (comp_att_pairs(state) > comp_att_pairs(cheapest_climbing(state,comp_att_pairs))):
    	state = cheapest_climbing(state,comp_att_pairs)
    final_state = state
#    print str(final_state)
    return final_state
        
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    final_state = []
    state = get_rand_st(n)
#    for k in state:
#    	print str(k)+" ",
#    print ""
#    final_state = state[:]
    state  = hill_descending(state,comp_att_pairs) 
       
#    for k in state:
#    	print str(k)+" ",
#    print ""
    
    while (comp_att_pairs(state) != 0):
    	state = get_rand_st(n)
	state = hill_descending(state,comp_att_pairs)
    # Your code here
    final_state = state
#    for k in state:
#    	print "finals: "+ str(k)+" ",
    return final_state



