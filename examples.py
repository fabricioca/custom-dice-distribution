import CustomDiceDistribution as cdd

#TODOs
# Exportar .csv com tabelas com os valores de probabilidade

def copyDice(dice, number = 1):
    dices = []
    for _ in range(number):
        dices.append(dice)

    return dices

def graphs(dices):
    rolls = cdd.diceRolls(dices)

    prob = cdd.diceProb(rolls)
    cdd.diceProbGraph(prob)

    probUpper = cdd.diceProbUpper(rolls)
    cdd.diceProbGraph(probUpper)

    probLower = cdd.diceProbLower(rolls)
    cdd.diceProbGraph(probLower)

def diceProb(dice, number = 1): 
    dices = copyDice(dice, number)
    graphs(dices)



regularDice = [".","..","...","....",".....","......"]
terrorDice = ["x","-","-","-","s","ss"]
arkaranHorrorDice = ["-","-","-","-","s","s"]
MansionsOfMadnessDice = ["-","-","-","c","c","s","s","s"]

# Terror Dice 5
diceProb(terrorDice, number = 5)

# Regular Dice 2
# diceProb(regularDice, number = 2)

# Regular Dice 3
# diceProb(regularDice, number = 3)

# Arkahan Horror 5
# diceProb(arkaranHorrorDice, number = 5)

# Mansions of Madness 3
# diceProb(MansionsOfMadnessDice, number = 3)


    
    