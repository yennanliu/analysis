def optimal_path(nodes, distances):
    """
    : input : 
        e.g. nodes = ('A', 'B', 'C')
        e.g. distances = {'A':{'B':1,'C':2},'B': {'C':2}, 'C': {'A':1}}

    """
    unvisited = {node: None for node in nodes} # use None as infinite
    visited = {}  # record visited nodes 
    current = 'A' # find the distance between node A and others 
    currentDistance = 0
    unvisited[current] = currentDistance # distance(A,A) = 0 

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: 
                continue # if aleady visited, break this loop 
            newDistance = currentDistance + distance # new distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance: # if distance(a,b) is infinite or < original distance
                unvisited[neighbour] = newDistance # update distance
        visited[current] = currentDistance # in case this node already visited, record it 
        del unvisited[current] # delete the node haven't visited from the unvisit dict 
        if not unvisited: 
            break # if all nodes are visited, break the loop 
        candidates = [node for node in unvisited.items() if node[1]] # find all unvisited points 
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return current, currentDistance, visited, unvisited
