from bs4 import BeautifulSoup
import re

rawData = open("dataPretty.html", "r")
qB = open("qBNames.html", "r")
stats = BeautifulSoup(rawData.read(), "html.parser")
people = BeautifulSoup(qB.read(), "html.parser")

data = stats.find_all("div", {'class' : "kyber-table-body-cell kyber-table-body-cell--align-right"})

names = people.find_all("a", {'class' : ""})

#for message in data:
#    try:
#        wantedData = int(message.text.strip())
#    except:
#        continue
#    print(wantedData)

for eachName in names:
    wantedName = eachName.text.strip()
    print(wantedName)
