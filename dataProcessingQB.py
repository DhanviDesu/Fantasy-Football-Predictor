from bs4 import BeautifulSoup
import re
import operator
import csv

rawData = open("dataPretty.html", "r")
qB = open("qBNames.html", "r")
stats = BeautifulSoup(rawData.read(), "html.parser")
people = BeautifulSoup(qB.read(), "html.parser")

data = stats.find_all("div", {'class' : "kyber-table-body-cell kyber-table-body-cell--align-right"})

names = people.find_all("a", {'class' : ""})

statsList = []
namesList = []
fullDict = {}
finalDict = {}
finalRank = []
weights = [40, 30, -10, 25, 15]

#formula:  rank each person based on each cat, then rank by highest ave in each cat, (lowest in inteceptions), 
#35*pYards+25 * ptd + 10*int + 20*ryards + 10*rtd




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
    sortedFinalList = []

    counter = 1
    for key in sortedFinal:
        key = list(key)
        key[1] = counter
        sortedFinalList.append(key)
        counter += 1

    finalRank = sortedFinalList
    return finalRank

def prettyPrint():
    download_dir = "qbCSV.csv" #where you want the file to be downloaded to 

    csv = open(download_dir, "w") 
    #"w" indicates that you're writing strings to the file

    bestPlayer = "\n You should pick up " + finalRank[0][0] + " for this gameweek!\n\n"
    csv.write(bestPlayer)

    #columnTitleRow = "rank    name\n"
    #csv.write(columnTitleRow)

    for item in finalRank:
        name = item[0]
        rank = str(item[1])
        if item[1] < 10:
            row = "  " + rank + "     " + name + "\n"
        else:
            row = " " + rank + "     " + name + "\n"
        csv.write(row)
    csv.write("\n")


def setup():
    for message in data:
        try:
            wantedData = int(message.text.strip())
        except:
            continue
    
        statsList.append(wantedData)

    for eachName in names:
        wantedName = eachName.text.strip()
        namesList.append(wantedName)

    # 3(pyards) 4(ptd) 5(int) 7(ryards) 8(rtd)
    counter = 0
    for name in namesList:
        fullDict[name] = [ statsList[10*counter + 3] ]
        index = 0
        while index < 10:
            if index == 4 or index == 5 or index == 7 or index == 8:
                fullDict[name].append( statsList[10*counter + index] )
            index += 1
        counter += 1





#print(finalRank)
setup()
finalRank = rankings(fullDict)
prettyPrint()

#print(fullDict)
#getPosition (2, fullDict)


#print(statsList)
#print(namesList)
