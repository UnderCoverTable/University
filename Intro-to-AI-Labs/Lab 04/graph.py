#Name:
#Roll No.:

class Graph:
    """
    The purpose of the class is to provide a clean way to define a graph for
    a searching algorithm:
    """

    def __init__(self):
        self.edges = {} # dictionary of edges NODE: NEIGHBOURS
        self.weights = {} # dictionary of NODES and their COSTS 
        
        # add a dictionary to store heuristics for nodes
        self.heuristics = {}

    def neighbours(self, node):
        """
        The function returns the neighbour of the node passed to it,
        which is essentially the value of the key in the edges dictionary.

        :params node: (string) a node in the graph

        :return: (list) neighbouring nodes
        """

        return self.edges[node]

    def get_cost(self, from_node, to_node):
        """
        Gets the cost of a connection between adjacent nodes.

        :params from_node: (string) starting node
        :params to_node: (string) ending node

        :return: (int) 
        """
        
        return self.weights[(from_node + to_node)]

    def get_h(self, node):
        """
        This function will give us the heuristic from the node to goal.

        :params node: (String) current node / any node

        :return: (int) heuristic to the goal
        """

        # write your code below 
        return self.heuristics[node]


if __name__ == "__main__":
    # testing out the graph class
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
    graph.heuristics = {"A":9,"A":9,"B":4,"C":2,"D":5,
                        "E":3,"G":0
    }
    # test functions from the class
    print(graph.neighbours("A"))
    print(graph.get_cost("S","D"))
    print(graph.get_h("D"))