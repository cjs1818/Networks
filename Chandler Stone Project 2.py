'''
Chandler Stone
Philip Brown
CS 4740.001
1 March 2022
'''

#Import libraries
from matplotlib import pyplot as plt
from animate_schelling import create_example, display_animation, load_json_file
from collections import deque
from statistics import mean
import numpy as np
import networkx as nx
import random

#Main simulation function with given parameters                             
def simulate_model(n, red_blue_split, t, pct_empty):

    #Initialize grid
    grid = np.zeros((n, n), 'U1')
    
    #Find total number of empty spots
    totalEmpty = (n * n) * pct_empty

    #print(totalEmpty)

    #Find total number of blue agents
    totalBlue = ((n * n) - totalEmpty) 

    #Fill grid with empty spots
    while(totalEmpty > 0):
        row = random.randint(0, (n - 1))
        column = random.randint(0, (n - 1))
        grid[row, column] = 'E'
        totalEmpty -= 1

    #Fill grid with blue agents
    while(totalBlue > 0):
        row = random.randint(0, (n - 1))
        column = random.randint(0, (n - 1))

        if grid[row, column] == '':
            grid[row, column] = 'B'
            totalBlue -= 1

    emptyLocations = []

    #Fill grid with red agents
    for i in range(n):
        for j in range(n):

            if grid[i, j] == '':
                grid[i, j] = 'R'

            elif grid[i, j] == 'E':
                emptyLocations.append((i, j))

    #print(emptyLocations)
    
    #List for unhappy agents
    unhappyAgents = []

    #Iterate through grid to find all unhappy agents
    for i in range(n):
        for j in range(n):

            currentAgent = grid[i, j]

            fraction  = 0
            totalNeighbors = 0

            if currentAgent == 'E':
                continue

            else:
                similarNeighbors = 0
                neighbors = get_neighbors(i, j, n)
                
                for each in neighbors:
                    if (grid[each] == 'R' or grid[each] == 'B'):
                        totalNeighbors += 1
                            
                        if (grid[each] == currentAgent):
                            similarNeighbors = similarNeighbors + 1

                if (totalNeighbors == 0):
                    continue

                else:
                    fraction = similarNeighbors / totalNeighbors
                
                    #Check if the fraction of neighbors is less than threshold
                    if fraction < t:
                        unhappyAgents.append((i, j))

                #print(similarNeighbors)

    #Print the staring grid
    print(np.matrix(grid))
    #print(unhappyAgents)
    loopCounter = 0
    loopCounterList1 = []
    ctfValues1 = []
    graphStuff = []
    
    #Iterate through the unhappy agents list until it is empty or the loop has iterated 7000 times
    while (len(unhappyAgents) != 0 and loopCounter < 7000):

        count = len(unhappyAgents) - 1
        loopCounter += 1

        #print(count)
        
        #Find a random empty location
        randomNumber = random.randint(0, len(emptyLocations) - 1)
        randomEmpty = emptyLocations[randomNumber]

        #print(randomEmpty)

        #Swap the agents
        currentLocation = unhappyAgents[count]
        currentChar = grid[currentLocation]

        #print(currentLocation)
        #print(currentChar)

        #Empty the old location
        grid[randomEmpty] = currentChar
        grid[currentLocation] = 'E'

        #print(np.matrix(grid))

        #Delete the unhappy agent from the list and empty location from it's list
        del unhappyAgents[count]
        #print(unhappyAgents)
        del emptyLocations[randomNumber]
        emptyLocations.append(currentLocation)
        count -= 1

        #Check again to see if the agent is happy in new location
        for i in range(n):
            for j in range(n):

                currentAgent = grid[i, j]

                fraction  = 0
                totalNeighbors = 0

                if currentAgent == 'E':
                    continue

                else:
                    similarNeighbors = 0
                    neighbors = get_neighbors(i, j, n)
                
                    for each in neighbors:
                        if (grid[each] == 'R' or grid[each] == 'B'):
                            totalNeighbors += 1
                            
                            if (grid[each] == currentAgent):
                                similarNeighbors = similarNeighbors + 1

                    if (totalNeighbors == 0):
                        continue

                    else:
                        fraction = similarNeighbors / totalNeighbors
                
                        #If the agent is still unhappy, add it back onto the list
                        if fraction < t:
                            unhappyAgents.append((i, j))
                            count += 1

                    #print(similarNeighbors)

        #print(grid[currentLocation])

        #Calculate the CTF
        ctfValues1.append(calculate_CTF(grid, n))

        #Loop counter list for graphing purposes
        loopCounterList1.append(loopCounter)
        #print('Part 1')

    #Deliverable 3 CTF calculation
    endCTF = calculate_CTF(grid, n)

    print(np.matrix(grid))
    #print(unhappyAgents)
    #print(ctfValues1)

    return endCTF

    '''
    # Plot and show the graph for deliverable 2
    plt.plot(loopCounterList1, ctfValues1, color = 'red')
    plt.plot(loopCounterList2, ctfValues2, color = 'blue')
    plt.plot(loopCounterList3, ctfValues3, color = 'green')
    plt.plot(loopCounterList4, ctfValues4, color = 'purple')
    plt.plot(loopCounterList5, ctfValues5, color = 'orange')
    plt.xlabel('Loop Counter')
    plt.ylabel('CTF Values')
    plt.show()
    '''
        
#Iterate through the grid and neighbors to calculate CTF
def calculate_CTF(grid, n):

    ctf = 0
    ctfTotalNeighbors = 0
    ctfCrossNeighbors = 0

    for i in range(n):
        for j in range(n):
            
            currentAgent = grid[i, j]

            if currentAgent == 'E':
                continue

            else:
                neighbors = get_neighbors(i, j, n)

                for each in neighbors:
                    if (grid[each] == 'R' or grid[each] == 'B'):
                        ctfTotalNeighbors += 1
                            
                        if (grid[each] != currentAgent):
                            ctfCrossNeighbors += 1

    ctf = ctfCrossNeighbors / ctfTotalNeighbors
    return ctf

def average_CTF(red_blue_split, t, pct_empty):

    #List to hold the averages
    averageCTFList = []

    #Simulate the model 10 times and calculate the average
    print('Part 1')
    averageCTFList.append(simulate_model(30, red_blue_split, t, pct_empty))
    print('Part 2')
    averageCTFList.append(simulate_model(30, red_blue_split, t, pct_empty))
    print('Part 3')
    averageCTFList.append(simulate_model(30, red_blue_split, t, pct_empty))
    print('Part 4')
    averageCTFList.append(simulate_model(30, red_blue_split, t, pct_empty))
    print('Part 5')
    averageCTFList.append(simulate_model(30, red_blue_split, t, pct_empty))
    print('Part 6')
    averageCTFList.append(simulate_model(30, red_blue_split, t, pct_empty))
    print('Part 7')
    averageCTFList.append(simulate_model(30, red_blue_split, t, pct_empty))
    print('Part 8')
    averageCTFList.append(simulate_model(30, red_blue_split, t, pct_empty))
    print('Part 9')
    averageCTFList.append(simulate_model(30, red_blue_split, t, pct_empty))
    print('Part 10')
    averageCTFList.append(simulate_model(30, red_blue_split, t, pct_empty))
    
    averageCTF = mean(averageCTFList)
    return averageCTF

#Function for finding and returning lists of neighbors based on an agent's location on the grid
def get_neighbors(i, j, n):
    
    if i == 0 and j == 0 :
        return [(0, 1), (1, 1), (1, 0)]
    elif i == n - 1 and j == n - 1 :
        return [(n - 2, n - 2), (n - 1, n - 2), (n - 2, n - 1)]
    elif i == n - 1 and j == 0:
        return [(i - 1, j), (i, j + 1), (i - 1, j + 1)]
    elif i == 0 and j == n - 1:
        return [(i + 1, j), (i, j - 1), (i + 1,j - 1)]	
    elif i == 0:
        return [(i, j - 1), (i, j + 1),(i + 1, j), (i + 1, j - 1), (i + 1, j + 1)]
    elif j == 0:
        return [(i - 1, j), (i + 1, j), (i, j + 1), (i - 1, j + 1), (i + 1, j + 1)]
    elif i == n - 1:
        return [(i, j - 1), (i, j + 1), (i - 1, j), (i - 1, j - 1), (i - 1, j + 1)]
    elif  j == n - 1:
        return [(i - 1, j), (i + 1, j), (i - 1, j - 1), (i, j - 1), (i + 1, j - 1)]
    else:
        return [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1),(i - 1, j),(i + 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]

#Deliverable 1 simulation
simulate_model(5, 0.5, 0.3, 0.8)

'''
#Average CTF lists for graphing purposes
totalAverageCTF = []
testValues = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

#Deliverable 3, run 10 simulations for each value using average_CTF
print("0.1")
totalAverageCTF.append(average_CTF(0.5, 0.3, 0.1))
print("0.2")
totalAverageCTF.append(average_CTF(0.5, 0.3, 0.2))
print("0.3")
totalAverageCTF.append(average_CTF(0.5, 0.3, 0.3))
print("0.4")
totalAverageCTF.append(average_CTF(0.5, 0.3, 0.4))
print("0.5")
totalAverageCTF.append(average_CTF(0.5, 0.3, 0.5))
print("0.6")
totalAverageCTF.append(average_CTF(0.5, 0.3, 0.6))
print("0.7")
totalAverageCTF.append(average_CTF(0.5, 0.3, 0.7))
print("0.8")
totalAverageCTF.append(average_CTF(0.5, 0.3, 0.8))
print("0.9")
totalAverageCTF.append(average_CTF(0.5, 0.3, 0.9))
print("1.0")
totalAverageCTF.append(average_CTF(0.5, 0.3, 1))

# Plot and show the graphs for deliverable 3
plt.plot(testValues, totalAverageCTF, color = 'blue')
plt.xlabel('Test Values')
plt.ylabel('Average CTF Values')
plt.show()
'''
