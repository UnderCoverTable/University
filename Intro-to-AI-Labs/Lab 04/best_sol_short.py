# importing helper classes
from graph import Graph

def a_star_search(graph, start_node, goal_node):
    """
    The function should take in the graph defined along with the
    start and goal nodes and print out the shorted path according 
    to the A* Search Algorithm.

    NOTE: print the path and cost

    :params graph: (Graph) defined graph
    :params start_node: (String) starting node from graph
    :params goal_node: (String) goal node from the graph

    :return : None
    """

    # write your code below

    total_cost = 0
    route = []
    node = start_node
    while node != goal_node:
  
        node_neighbours = graph.neighbours(node) # List of neighbours of the current node
        store_node_vals = {} # store the Node : cost + heuristic
            
       

        for neighbour in node_neighbours: # Iterates through the neighbours of the current node
                
            # If the neighbour is not the goal node. It just updates the dict with node and its f(n)
            f = graph.get_h(neighbour) + graph.get_cost(node,neighbour)
            store_node_vals[node+neighbour] = f


        cost_heu = store_node_vals.values() # List of the f(n) of each node

        if min(cost_heu) == max(cost_heu): # In the case that 2 nodes have the same f(n)
            
            min_cost = min([graph.get_cost(node,n) for n in node_neighbours]) # In this case we get the node with min cost instead
            
            for new_node in node_neighbours:
                if min_cost == graph.get_cost(node,new_node):
                    min_node = node+new_node # We get the node that has the minimum cost

            # Update botht cost and route list
            total_cost += graph.get_cost(min_node[0],min_node[1])
            route.append(min_node)

            # print node, cost and heuristic
            print(f"{min_node} --> Cost({graph.get_cost(min_node[0],min_node[1])}) + Heuristic({graph.get_h(min_node[1])})",
                  f" =  {graph.get_cost(min_node[0],min_node[1]) + graph.get_h(min_node[1])}"
            )

            node = min_node[1] # Updates the current node
        
        else:
            # If the f(n) of 2 nodes is different, we simple take the one which is minimum
            min_node = min(cost_heu)

            # We get the next nodes key from its value from the dict
            next_node = list(store_node_vals.keys())[list(store_node_vals.values()).index(min_node)] 

            #Update total cost and route list
            total_cost += graph.get_cost(node ,next_node[1])
            route.append(node+next_node[1])

            # print node, cost and heuristic
            print(f"{node+next_node[1]} --> Cost({graph.get_cost(node,next_node[1])}) + Heuristic({graph.get_h(next_node[1])})",
                    f" =  {min_node}"
            )
            node = next_node[1] # UPdates the current node

        if node == goal_node:
            
            for place in route:
                    
                print(place[0], end = " --> ")
                if place[1] == goal_node:
                    print(goal_node)
                    break
            # Prints the final cost
            print(f"Total Cost = {total_cost}")
    

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
