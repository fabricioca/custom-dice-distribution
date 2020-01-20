import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import random

def diceProb(dices, sybols = [], title = "", n = 10000):

    if(len(sybols) == 0):
        sybols = {}
        for dice in dices:
            for face in dice:
                for value in face:
                    sybols[value] = True
        sybols = list(sybols.keys())

    rollResults = {}
    for i in sybols:
        rollResults[i] = []

    for _ in range(n):
        rollResult = {}
        for i in sybols:
            rollResult[i] = 0
        
        for dice in dices:
            value = dice[random.randint(0, len(dice)-1)]
            for i in value:
                rollResult[i] += 1 

        for i in sybols:
            rollResults[i].append(rollResult[i])


    fig,ax =  plt.subplots(1,len(sybols), squeeze=False, figsize=(3*len(sybols),5))
    fig.suptitle(title)

    fig.tight_layout()

    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.5, hspace=None)

    for i in range(len(sybols)):
        distribution = Counter(rollResults[sybols[i]])

        keys = distribution.keys()
        values = [x/n for _,x in sorted(zip(keys, distribution.values()))]   
        
        keys = sorted(keys)
        keys = list(map(str, keys))
        
        ax[0][i].bar(keys, values)
        ax[0][i].set_title('Amount of "' + sybols[i] + '"')

    plt.show()
