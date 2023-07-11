#Name:
#Roll No.:

"""
Lab Task: 

For this lab you will be implementing A* (A Star Search) on a graph.
The picture of the graph can be found in assets directory.

For this lab you are provided with two helper classes.
One is for making a graph and the other one in an interface for Priority Queues.
You may open then these file, once opened you'll see descriptions for each function defined
and a testing code for the class in the main body. Kindly go through them to get comfortable 
with the functions

MAIN TASKS:

    1- Modify graph.py to have the ability to store heuristics
    2- Create a funciton 'get_h' in graph.py to get heuristic for a node : input will be a Node and output will be heuristic 
    3- Create the graph in graph.py to and check all the functions
    4- Replicate the graph in 'lab4.py'
    5- Implement A* function 

Your function should print the shortest path along with the cost of that path. 
A sample output is provided in the assests directory.
"""

# importing helper classes
from graph import Graph

def a_star_search(graph, start_node, goal_node):
    """
    The function should take in the graph defined along with the
    start and goal nodes and print out the shorted path according 
    to the A* Search Algorithm.

    NOTE: print the path and cost

    :params graph: (Graph) defined graph
    :params start_node: (String) starting node from graphs
    :params goal_node: (String) goal node from the graph

    :return : None
    """

    # write your code below
    total_cost = 0
    route = []
    node = start_node
    while node != goal_node:

        node_neigh = graph.neighbours(node) # gets the list of neighbours of the current node


        if graph.neighbours(node)[0] == goal_node: # if the neighbour of the current node has the goal in it
            
            # Prints the node, cost and heuristic
            print(f"{node+node_neigh[0]} --> cost({graph.get_cost(node,node_neigh[0])}) + heuristic({graph.get_h(node_neigh[0])})",
                  f" = {graph.get_h(node_neigh[0]) + graph.get_cost(node,node_neigh[0])}"
            )            
            # Total cost and route list is updated
            total_cost += graph.get_cost(node,goal_node)
            route.append(node+node_neigh[0])
            route.append(goal_node)

            # Route is printed
            for node in route:
                if node == goal_node:
                    print(node[0])
                    break
                print(node[0], end = " --> ")

            # Total cost is printed
            print(f"Total Cost = {total_cost}")
            break

       
        # Extracts both neighbours
        # Then adds the cost and heuristic for each node
        node1 = graph.get_h(node_neigh[0]) + graph.get_cost(node,node_neigh[0]) 
        node2 = graph.get_h(node_neigh[1]) + graph.get_cost(node,node_neigh[1])

        if node1 == node2: #if heuristic + cost is equal it chooses the one with least actual cost
            least_cost = min(graph.get_cost(node,node_neigh[0]),graph.get_cost(node,node_neigh[1]))

            if graph.get_h(node_neigh[0]) + least_cost == node1:
                next_node = node1
                print(f"{node+node_neigh[0]} --> cost({graph.get_cost(node,node_neigh[0])}) + heuristic({graph.get_h(node_neigh[0])})",
                    f" = {graph.get_h(node_neigh[0]) + graph.get_cost(node,node_neigh[0])}"
                )

                total_cost += graph.get_cost(node,node_neigh[0]) #total cost is updated
                route.append(node+node_neigh[0]) # adds the nodes to list
                node = node_neigh[0] # updates the current node to move forward

            else:
                next_node = node2
                # Prints the node, cost and heuristic 
                print(f"{node+node_neigh[1]} --> cost({graph.get_cost(node,node_neigh[1])}) + heuristic({graph.get_h(node_neigh[1])})",
                    f" = {graph.get_h(node_neigh[1]) + graph.get_cost(node,node_neigh[1])}"
                )         

                total_cost += graph.get_cost(node,node_neigh[1])#total cost is updated
                route.append(node+node_neigh[1]) # adds the nodes to list
                node = node_neigh[1] # updates the current node to move forward
        
        else:
            next_node = min(node1,node2) # Minimum of both these nodes is chosen


            if next_node == node1:
                # Prints the node, cost and heuristic 
                print(f"{node+node_neigh[0]} --> cost({graph.get_cost(node,node_neigh[0])}) + heuristic({graph.get_h(node_neigh[0])})",
                    f" = {graph.get_h(node_neigh[0]) + graph.get_cost(node,node_neigh[0])}"
                )

                total_cost += graph.get_cost(node,node_neigh[0]) #total cost is updated
                route.append(node+node_neigh[0]) # adds the nodes to list
                node = node_neigh[0] # updates the current node to move forward
                
            else:
                # Prints the node, cost and heuristic 
                print(f"{node+node_neigh[1]} --> cost({graph.get_cost(node,node_neigh[1])}) + heuristic({graph.get_h(node_neigh[1])})",
                    f" = {graph.get_h(node_neigh[1]) + graph.get_cost(node,node_neigh[1])}"
                )         

                total_cost += graph.get_cost(node,node_neigh[1])#total cost is updated
                route.append(node+node_neigh[1]) # adds the nodes to list
                node = node_neigh[1] # updates the current node to move forward
        



if __name__ == "__main__":

    # Defining Graph
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {"S":["A","D"],"A":["B","C"],"B":["C","E"],
                    "C":["G"],"D":["B","E"],"E":["G"]
    }
    
    # setting up connection costs
    graph.weights = {"SA":3,"AB":5,"AC":10,
                    "BC":2,"SD":2,"DB":1,"BE":1,"DE":4,
                    "EG":3,"CG":4
    }

    # setting up heuristics
    graph.heuristics = {"S":7,"A":9,"B":4,"C":2,"D":5,
                        "E":3,"G":0
    }

    # a_star Function Test
    a_star_search(graph, 'S', 'G') 
