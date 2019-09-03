from bs4 import BeautifulSoup
#mport urllib2

data = open("Fantasy Stats | PFF.html", "r")
#pretty = open("dataPretty.html", "w")
qBNames = open("qBNames.html", "w")


if data.mode == "r":
    contents = data.read()

soup = BeautifulSoup(contents, "html.parser")

qBNames.write( soup.prettify() )
