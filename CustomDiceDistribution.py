import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import random
import math

def getSymbols(dices):
    symbols = {}
    for dice in dices:
        for face in dice:
            for value in face:
                symbols[value] = True
    symbols = list(symbols.keys())

    return symbols

def diceRolls(dices, symbols = [], n = 10000):

    if(len(symbols) == 0):
        symbols = getSymbols(dices)

    rollResults = {}
    for i in symbols:
        rollResults[i] = []

    for _ in range(n):
        rollResult = {}
        for i in symbols:
            rollResult[i] = 0
        
        for dice in dices:
            value = dice[random.randint(0, len(dice)-1)]
            for i in value:
                rollResult[i] += 1 

        for i in symbols:
            rollResults[i].append(rollResult[i])

    return rollResults

def diceProb(rolls):   
    prob = {}

    for i in rolls.keys():
        distribution = Counter(rolls[i])

        n = len(rolls[i])

        keys = distribution.keys()
        values = [x/n for _,x in sorted(zip(keys, distribution.values()))]   
        
        keys = sorted(keys)

        prob[i] = [keys,values]

    return prob

def diceProbUpper(rolls):
    prob = diceProb(rolls)

    for i in list(prob.keys()):
        values = []

        for j in range(len(prob[i][0])):
            sum = 0
            for k in range(len(prob[i][0])):
                if (prob[i][0][k] >= prob[i][0][j]):
                    sum += prob[i][1][k]
            values.append(sum)

        prob[i][1] = values

    return prob

def diceProbLower(rolls):
    prob = diceProb(rolls)

    for i in list(prob.keys()):
        values = []

        for j in range(len(prob[i][0])):
            sum = 0
            for k in range(len(prob[i][0])):
                if (prob[i][0][k] <= prob[i][0][j]):
                    sum += prob[i][1][k]
            values.append(sum)

        prob[i][1] = values

    return prob

def diceProbGraph(data, symbols = [], title = ""):

    if (len(symbols) == 0):
        symbols = list(data.keys())

    fig,ax =  plt.subplots(1,len(symbols), squeeze=False, figsize=(3*len(symbols),5))
    
    if(title != ""):
        fig.suptitle(title)

    fig.tight_layout()

    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.5, hspace=None)

    for i in range(len(symbols)):
        graphData = data[symbols[i]]

        keys = list(map(str, graphData[0]))
        
        ax[0][i].bar(keys,graphData[1])
        ax[0][i].set_title('Amount of "' + symbols[i] + '"')

    plt.show()
