"""
Intro. To AI

Lab 8: Hill Climb Algorithm


In this lab you'll be implementing a Hill Climb algorithm on a very simple Graph.

Hill climb is a heurisitc search used for mathematical optimization problems in the field of Artificial Intelligence. Given a large set 
of inputs and a good heuristic function, it tried to find a sufficiently
good solution to the problem. This solution may not be the global maximum.

In this lab you'll be implementing a basic version of the algorithm on 
a graph. For representing a Graph you may modify the class in the 
graph.py file accordingly.

In this task you will create a function named hill_climb_search() that
will take in the graph along with the start and the goal node. The 
function will print the path it took after reaching the goal node.

The graph that you will work on is as follows, where the representation
includes the node and the heuristic of that (node, heuristic):

# A is the root node with B, C, D as successors
(A,3) -> (B, 4), (C, 6), (D, 5) 
(B,4) -> (E, 3), (F, 2) 
(C,6) -> (G, 7), (H, 8)
(D,5) -> (I, 6), (J, 7)
(H,8) -> (K, 9)

Solution: A -> C -> H -> K

Initial node to start is "A" and the goal node is "K"
"""

from graph import Graph


def hill_climb_search(graph,start,goal):

    node = start # Stores the current node we are on
    store_nodes_h = {} # stores nodes:heuristic in dictionary
    path = [start] # Stores the path 
    while node != goal: 

        node_neighbours = graph.neighbours(node) # Gets the neighbours of the node we are on
    
        for neighbour in node_neighbours: # Iterates through those neighbors one by one and stores in dict, node:heuristic 

            heuristic = graph.get_h(neighbour)
            store_nodes_h[neighbour] = heuristic

        max_heuristic = max(store_nodes_h.values()) # Stores the max heuristic
        next_node = list(store_nodes_h.keys())[list(store_nodes_h.values()).index(max_heuristic)] # Gets the key from value(node from heuristic)
        node = next_node # updates new to the next one
        path.append(node) # Appends new node in list to store our path

    for i in range(0,len(path)): # Once all nodes are explored, we print the final path
        if i == len(path)-1:
            print(goal)
            break
 
        print(path[i],end = " --> ")
        



if __name__ == "__main__":

    # Defining Graph
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {"A":["B","C","D"],"B":["E","F"],
                    "C":["G","H"],"D":["I","J"],"H":["K"]
    }
    

    # setting up heuristics
    graph.heuristics = {"A":9,"B":4,"C":6,"D":5,
                        "E":3,"F":2,"G":7,"H":8,"I":6,"J":7,"K":9
    }

    # a_star Function Test
    hill_climb_search(graph, 'A', 'K') 
