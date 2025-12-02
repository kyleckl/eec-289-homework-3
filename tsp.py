# import packages
import time
import math
import random

# file parsing
def parseTSPFile(f):
    # dictionary to represent graph info
    G ={}

    with open(f, 'r') as file:
        lines = file.readlines()

        # get number of nodes
        numNodes = int(lines[0].strip())
    
        print("Number of nodes:", numNodes)

        # skip the second line that are just column names
        startIndex = 0
        for i, line in enumerate(lines):
            parts = line.strip().split()
            if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
                startIndex = i
                break
        

        for i in range(startIndex, len(lines)):
            parts = lines[i].strip().split()
            # cast to appropriate type since its a string
            # subtract 1 to get 0 index
            V1 = int(parts[0]) - 1
            V2 = int(parts[1]) - 1
            E = float(parts[2])

            if V1 not in G:
                G[V1] = {}
            if V2 not in G:
                G[V2] = {}
            
            G[V1][V2] = E
            G[V2][V1] = E
    return G, numNodes

# greedy approach
# choose the nearest unvisited neighbor from current node
def tspGreedy(G, numNodes):
    startNode = 0
    path = [startNode]
    visited = set([startNode])
    totalCost = 0.0

    currentNode = startNode
    # keep looping until the path we have has all the nodes
    while len(path) < numNodes:
        nextNode = None
        shortestDistance = float('inf')
        for n, d in G.get(currentNode, {}).items():
            if n not in visited and d < shortestDistance:
                shortestDistance = d
                nextNode = n
        
        if nextNode is not None:
            path.append(nextNode)
            visited.add(nextNode)
            currentNode = nextNode
            totalCost += shortestDistance
        else:
            break
    
    # return to start
    if len(path) == numNodes:
        returnDist = G[currentNode][startNode]
        totalCost += returnDist
        
    return path, totalCost

# hill climbing approach
def tspHillClimbing(G, numNodes, initialPath, initialCost, timeLimit = 55):
    # swap edges 2-opt and accept changes that improve cost
    currPath = list(initialPath)
    currCost = initialCost

    bestPath = list(currPath)
    bestCost = currCost

    visitedCycles = 0
    startTime = time.time()

    # keep running until time limit is reached
    while(time.time() - startTime) < timeLimit:
        visitedCycles = visitedCycles + 1

        i, j = sorted(random.sample(range(1, numNodes), 2))

        # A --> B --> C --> D
        A = currPath[i - 1]
        B = currPath[i]
        C = currPath[j]
        D = currPath[(j + 1) % numNodes]

        # check if distance changed
        distRemoved = G[A][B] + G[C][D]
        dAdded = G[A][C] + G[B][D]

        newCost = currCost - distRemoved + dAdded

        # check to see if the new cost is better (lesser)
        # if so, swap
        if newCost < currCost:
            currPath[i:j+1] = reversed(currPath[i:j+1])
            currCost = newCost
            bestCost = currCost
            bestPath = list(currPath)
    
    return bestPath, bestCost, visitedCycles

# main
if __name__ == "__main__":
    # parse file(s)
    files = ["TSP_1000_euclidianDistance.txt", "TSP_1000_randomDistance.txt"]
    result = []

    for f in files:
        G, numNodes = parseTSPFile(f)
        print("Finished parsing graph from file", f)

        # find greedy solution
        greedyPath, greedyCost = tspGreedy(G, numNodes)
        print("Greedy solution for file found, cost:", greedyCost)