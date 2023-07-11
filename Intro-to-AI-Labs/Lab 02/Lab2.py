def BFS(tree):
    visited_list = []
    parents = list(tree.keys()) # Creates a list of all the parents in the tree

    root = parents[0] 
    visited_list.append(root) # adds the root to the visited list

    for i in range(0,len(parents)): # Iterates through each parent
        for child in tree[parents[i]]: # Iterates through each parents children
            if child not in visited_list:
                visited_list.append(child) # adds child to visited list
        
    return visited_list

def DFS(tree, node, visited_list=None):

    if visited_list is None: # Creates a list to store visited nodes in dfs order, when fucntion runs the first time
        root = list(tree.keys())[0]
        visited_list = [root] # Initialises list with the root

    for child in tree[node]: # Goes through each child till it reaches one without a parent or a leaf
        if child not in visited_list: # if the node isnt in visited, its added there
            visited_list.append(child)
        if child not in tree.keys(): # To avoid key errors
            continue
        else:
            DFS(tree, child,visited_list) # recrusive call to the next node

    return visited_list 


if __name__ == '__main__':
    tree = {1:[2,3,4], 2:[5,6], 4:[7,8], 5:[9,10] ,7:[11,12]}

    print("Breadth First Search:")
    bfs_order = BFS(tree)

    for node in bfs_order:
        print(node, end = ", ")

    print("\nDepth First Search:")
    dfs_order = DFS(tree,1)

    for node in dfs_order:
        print(node, end = ", ")

