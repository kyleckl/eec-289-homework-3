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
    
        print("Nummber of nodes:", numNodes)

        # skip the second line that are just column names
        startIndex = 0
        for i, line in enumerate(lines):
            parts = line.strip().split()
            if len(parts) == 3:
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