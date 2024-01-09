
class Card():

    def __init__(self, number, colour):
        self.number = number #integer
        self.colour = colour #string

    def getNumber(self):
        return self.number

    def getColour(self):
        return self.colour

cardvalues = [0]*30
textfile = open("CardValues.txt", "r")
for i in range(0, 30):
    storedata = textfile.readline().strip()
    cardvalues[i] = storedata

player1 = [0]*4
alreadyChosen = [0]*30
cards = 0
def chooseCard():
    for i in range(0, 4):
        if player1[i] > 0 :
            cards = cards + 1
        if cards == 4:
            print("You already have max cards")
            break
    index = 0
    counter = 0
    chosen = int(input("What number of card do you want?"))
    while chosen >=30 or chosen <= 1:
        chosen = int(input("Invalid number, select one from 1-30"))
    while counter != 30:
        counter = 0
        chosen = int(input("Card already selected, choose another one"))
        for i in range(0, 30):
            if chosen != cardvalues[i]:
                counter = counter + 1

    for i in range(0, 30):
        if cardvalues[i] == chosen:
            alreadyChosen[index] = chosen
            index = index + 1
            return i


for i in range(0, 4):
    print(player1[i], cardvalues[player1[i]+1])




