import CustomDiceDistribution as cdd

# # Terror Dice
sybols = ["x","-","s"]
terrorDice = ["x","-","-","-","s","ss"]
dices = [terrorDice, terrorDice, terrorDice, terrorDice, terrorDice]
cdd.diceProb(dices, title="5 Terror Dice Probability")

# # Regular Dice
# regularDice = ["x","xx","xxx","xxxx","xxxxx","xxxxxx"]
# dices = [regularDice, regularDice]
#diceProb(dices, title="2 Regular Dice Sum")

# Arkahan Horror
ahDice = ["-","-","-","-","s","s"]
dices = [ahDice, ahDice]
cdd.diceProb(dices, title="2 A.H. Dice")