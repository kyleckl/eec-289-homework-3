# import packages
import time
import math
import random

# file parsing
def parseTSPFile(f):
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
            node1 = int(parts[0])
            node2 = int(parts[1])
            distance = float(parts[2])
