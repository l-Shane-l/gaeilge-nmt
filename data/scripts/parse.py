from bs4 import BeautifulSoup

f = open("../raw-data/en-ga.roam.tmx", "r")
#f = open("../raw-data/snippet.tmx", "r")

soup = BeautifulSoup(f)


f2 = open("../cleaned-data/en-ga.txt", "a")
f3 = open("../cleaned-data/en.txt", "a")
f4 = open("../cleaned-data/ga.txt", "a")

firstFile = True
for a in soup.find_all('seg'):
    f2.write(a.string + '\n')
    if(firstFile):
        f3.write(a.string + '\n')
        firstFile = not firstFile

    else:
        f4.write(a.string + '\n')
        firstFile = not firstFile


f.close()
f2.close()
f3.close()
f4.close()
