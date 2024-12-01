import os
os.system('cls')
def additionNächste(startwert):
    if startwert>2:
        startwert=startwert+2
        return startwert
    else:
        startwert=startwert+1
        return startwert
def prim(kandidat):
    divider = 2
    größerAlsWurzel= divider*divider
    while größerAlsWurzel <= kandidat:
        if((kandidat % divider)==0):
            return 0
        divider=additionNächste(divider)
        größerAlsWurzel= divider*divider
    return 1
maximum = input("Maximalwert? ")
maximum=int(maximum)
primListe=[]
for kandidat in range(2,maximum):
        if prim(kandidat)==1:
            print(kandidat,float(kandidat)/float(maximum)*100)
            primListe.append(kandidat)
        kandidat=additionNächste(kandidat)
print(primListe)