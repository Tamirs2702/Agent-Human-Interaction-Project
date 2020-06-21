# Reading an excel file
import csv

# max coins in each game
max_DictatorGame = 100
max_BanditGame = 100
max_CommonsDillemaGame = 40
max_PublicGoodDillemaGame = 40

# expected behavior (by Nash Equilibrium)
expectedDictatorGame = 0
expectedBanditGame = 100
expectedCommonsDillemaGame = 0
expectedPublicGoodDillemaGame = 40

# save the real behavior
real_behavior = 0
difference = 0
list = {}

# read the file row by row
with open(r"C:\Users\israe\OneDrive\temp\exp2.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Dictator Game
        print("Result in Dictator Game")
        print(row['DG.CHOICE'])
        real_behavior = row['DG.CHOICE']
        difference = abs(expectedDictatorGame - int(real_behavior)) / max_DictatorGame
        print("Difference in Dictator Game")
        print(difference)

        # Bandit Game
        print("Result in Bandit Game")
        print(row['BG.CHOICE'])
        real_behavior = row['BG.CHOICE']
        difference = abs(expectedBanditGame - int(real_behavior)) / max_BanditGame
        print("Difference in Bandit Game")
        print(difference)

        # Commons Dillema Game Game
        print("Result in Commons Dillema Game Game")
        print(row['CDG.CHOICE'])
        real_behavior = row['CDG.CHOICE']
        difference = abs(expectedCommonsDillemaGame - int(real_behavior)) / max_CommonsDillemaGame
        print("Difference in Commons Dillema Game Game")
        print(difference)

        # Public Good Dillema Game
        print("Result in Public Good Dillema Game")
        print(row['PGDG.CHOICE'])
        real_behavior = row['PGDG.CHOICE']
        difference = abs(expectedPublicGoodDillemaGame - int(real_behavior)) / max_PublicGoodDillemaGame
        print("Difference in Public Good Dillema Game")
        print(difference)

        # need to understand the model


# After we discover the model we can predict what the player will do in the next game
""" name = input("Enter your name : ")
print("Hi" + name + "!")
game = input("Which game did you play?")
coins = input("How much coins did you take?")
# calculate the next game action by the model
# print the result """