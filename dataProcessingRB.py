from bs4 import BeautifulSoup
import re
import operator

rawData = open("dataPretty.html", "r")
qB = open("qBNames.html", "r") # Change to RB names
stats = BeautifulSoup(rawData.read(), "html.parser")
people = BeautifulSoup(qB.read(), "html.parser")

data = stats.find_all("div", {'class' : "kyber-table-body-cell kyber-table-body-cell--align-right"})

names = people.find_all("a", {'class' : ""})

statsList = []
namesList = []
fullDict = {}
finalDict = {}
finalRank = []
weights = [25, 15, 10, 30, 20]

#formula:  rank each person based on each cat, then rank by highest ave in each cat, (lowest in inteceptions), 
#25*RCYards+15 * RCTD + 10*y/rc + 30*ryards + 20*rtd




def getPosition(statNum, toCalc):
    sortedPos = sorted(toCalc.items(), key=lambda e: e[1][statNum])
    i = 0
    while i < len(sortedPos):
        sortedPos[i][1][statNum] = len(sortedPos) -i
        i += 1
    
    return sortedPos

def rankings(toCalc):
    tempRank = []
    statType = 0
    while statType < 5:
        tempRank = getPosition(statType, toCalc)
        for player in tempRank:
            if player[0] not in finalDict:
                finalDict[player[0]] =  player[1][statType] * weights[statType]
            else:
                finalDict[player[0]] = finalDict[player[0]] + player[1][statType] * weights[statType]  
        statType += 1
    
    sortedFinal = sorted(finalDict.items(), key = lambda e: e[1])
    print(sortedFinal)

for message in data:
    try:
        wantedData = int(message.text.strip())
    except:
        continue
    #print(wantedData)
    statsList.append(wantedData)

for eachName in names:
    wantedName = eachName.text.strip()
    #print(wantedName)
    namesList.append(wantedName)

# 3(rcyards) 4(rctd) 5(y/rc) 7(ryards) 8(rtd)
counter = 0
for name in namesList:
    fullDict[name] = [ statsList[10*counter + 3] ]
    index = 0
    while index < 10:
        if index == 4 or index == 5 or index == 7 or index == 8:
            fullDict[name].append( statsList[10*counter + index] )
        index += 1
    counter += 1


rankings(fullDict)

