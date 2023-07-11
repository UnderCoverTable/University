import heapq

frontier = []
explored = []
graph = {
    "a":[(2,"b"),(1,"c")],
    "b":[(3,"f"),(4,"g")],
    "c":[(2,"d"),(3,"e")]
    }
graph_keys = list(graph.keys())
k = 0

explored.append(graph_keys[0])

def adjust_weight(gr,node):

    root = graph_keys[0]
    new_w = node[0]
    i = 0
    ii = 0

    while node[1] != root:
        key = graph_keys[list((gr).values()).index(node[1])]
        while gr[i][ii][1] != key:
            ii += 1
            if ii == 2:
                ii = 0
                i+= 1
        new_node = gr[i][ii]

        new_w += new_node[0]
        node = new_node
        
    print(node[1],new_w)
    


while len(explored) != 7:

    if explored[k] not in graph:
        explored.append(heapq.heappop(frontier)[1])
        

    else:
        node = graph[explored[k]]
       
        for i in range(0,len(node)):
        
            
            heapq.heappush(frontier,node[i])
        
        #print(explored)
        explored.append(heapq.heappop(frontier)[1])
        
        k += 1
    #print(f"Ex: {explored} + Fr: {frontier}")

    
   


