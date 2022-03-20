'''
Chandler Stone
Philip Brown
CS 4740.001
10 February 2022
'''

import itertools
import math
from collections import defaultdict
from matplotlib import pyplot as plt
import numpy as np
import networkx as nx

#PART 1

def randomGraph(n, p):

    G = nx.Graph()
    G.add_nodes_from(range(n))

    if p <= 0:
        return G
    
    if p >= 1:
        return nx.complete_graph(n, create_using = G)

    edges = itertools.combinations(range(n), 2)

    for i in edges:
        if np.random.rand() < p:
            G.add_edge(*i)
    
    return G

checkGraph = randomGraph(110, 0.02)
nx.draw(checkGraph, with_labels=True)
plt.show()

#PART 2

#Initialize arrays, each array represents a different chosen p-value with the number of components for each of the 10 random graphs
individualComp1 = [None] * 10
individualComp2 = [None] * 10
individualComp3 = [None] * 10
individualComp4 = [None] * 10
individualComp5 = [None] * 10
individualComp6 = [None] * 10
individualComp7 = [None] * 10
individualComp8 = [None] * 10
individualComp9 = [None] * 10
individualComp10 = [None] * 10

#Define number of nodes as n
n = 110

#Initialize allComp array to hold ALL numbers of components across all graphs and p-values
allComp = []

#Use randomGraph to do the math and fill the arrays
for i in range(10):
    individualComp1[i] = nx.number_connected_components(randomGraph(n,0.005))
    allComp.append(individualComp1[i])

    individualComp2[i] = nx.number_connected_components(randomGraph(n,0.01))
    allComp.append(individualComp2[i])

    individualComp3[i] = nx.number_connected_components(randomGraph(n,0.015))
    allComp.append(individualComp3[i])

    individualComp4[i] = nx.number_connected_components(randomGraph(n,0.02))
    allComp.append(individualComp4[i])

    individualComp5[i] = nx.number_connected_components(randomGraph(n,0.025))
    allComp.append(individualComp5[i])

    individualComp6[i] = nx.number_connected_components(randomGraph(n,0.03))
    allComp.append(individualComp6[i])

    individualComp7[i] = nx.number_connected_components(randomGraph(n,0.035))
    allComp.append(individualComp7[i])

    individualComp8[i] = nx.number_connected_components(randomGraph(n,0.04))
    allComp.append(individualComp8[i])

    individualComp9[i] = nx.number_connected_components(randomGraph(n,0.045))
    allComp.append(individualComp9[i])

    individualComp10[i] = nx.number_connected_components(randomGraph(n,0.05))
    allComp.append(individualComp10[i])

#Compute each of the averages for each p-value
compAvg1 = np.average(individualComp1)
compAvg2 = np.average(individualComp2)
compAvg3 = np.average(individualComp3)
compAvg4 = np.average(individualComp4)
compAvg5 = np.average(individualComp5)
compAvg6 = np.average(individualComp6)
compAvg7 = np.average(individualComp7)
compAvg8 = np.average(individualComp8)
compAvg9 = np.average(individualComp9)
compAvg10 = np.average(individualComp10)

#Fill array with averages for graph use
compAverages = [compAvg1, compAvg2, compAvg3, compAvg4, compAvg5, compAvg6, compAvg7, compAvg8, compAvg9, compAvg10]

#Fill array with tested p-values for graph use
pValues = [0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05]

#Initialize and fill allpValues to hold all p-values that correspond to values in allComp
allpValues = []

for i in range(10):
    allpValues.append(0.005)
    allpValues.append(0.01)
    allpValues.append(0.015)
    allpValues.append(0.02)
    allpValues.append(0.025)
    allpValues.append(0.03)
    allpValues.append(0.035)
    allpValues.append(0.04)
    allpValues.append(0.045)
    allpValues.append(0.05)


# Plot and show the graph
plt.plot(allpValues, allComp, 'o', pValues, compAverages, 'x')
plt.xlabel('P-Values')
plt.ylabel('Number of Components')
plt.show()


#PART 3

#Initialize arrays, each array represents a different chosen p-value with the number of components for each of the 10 random graphs
individualDeg1 = [None] * 10
individualDeg2 = [None] * 10
individualDeg3 = [None] * 10
individualDeg4 = [None] * 10
individualDeg5 = [None] * 10
individualDeg6 = [None] * 10
individualDeg7 = [None] * 10
individualDeg8 = [None] * 10
individualDeg9 = [None] * 10
individualDeg10 = [None] * 10

#Initialize allDeg array to hold ALL numbers of degrees across all graphs and p-values
allDeg = []

#Use randomGraph to do the math and fill the arrays
for i in range(10):
    individualDeg1[i] = np.average(randomGraph(n, 0.005).degree(i))
    allDeg.append(individualDeg1[i])

    individualDeg2[i] = np.average(randomGraph(n, 0.01).degree(i))
    allDeg.append(individualDeg2[i])

    individualDeg3[i] = np.average(randomGraph(n, 0.015).degree(i))
    allDeg.append(individualDeg3[i])

    individualDeg4[i] = np.average(randomGraph(n, 0.02).degree(i))
    allDeg.append(individualDeg4[i])

    individualDeg5[i] = np.average(randomGraph(n, 0.025).degree(i))
    allDeg.append(individualDeg5[i])

    individualDeg6[i] = np.average(randomGraph(n, 0.03).degree(i))
    allDeg.append(individualDeg6[i])

    individualDeg7[i] = np.average(randomGraph(n, 0.035).degree(i))
    allDeg.append(individualDeg7[i])

    individualDeg8[i] = np.average(randomGraph(n, 0.04).degree(i))
    allDeg.append(individualDeg8[i])

    individualDeg9[i] = np.average(randomGraph(n, 0.045).degree(i))
    allDeg.append(individualDeg9[i])

    individualDeg10[i] = np.average(randomGraph(n, 0.05).degree(i))
    allDeg.append(individualDeg10[i])

#Compute each of the averages for each p-value
degAvg1 = np.average(individualDeg1)
degAvg2 = np.average(individualDeg2)
degAvg4 = np.average(individualDeg3)
degAvg4 = np.average(individualDeg4)
degAvg5 = np.average(individualDeg5)
degAvg6 = np.average(individualDeg6)
degAvg7 = np.average(individualDeg7)
degAvg8 = np.average(individualDeg8)
degAvg9 = np.average(individualDeg9)
degAvg10 = np.average(individualDeg10)

#Fill array with averages for graph use
degAverages = [degAvg1, degAvg2, degAvg4, degAvg4, degAvg5, degAvg6, degAvg7, degAvg8, degAvg9, degAvg10]

# Plot and show the graph
plt.plot(allpValues, allDeg, 'o', pValues, degAverages, 'x')
plt.xlabel('P-Values')
plt.ylabel('Node Degrees')
plt.show() 
