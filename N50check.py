import numpy

def Openen(naam):
    bestand = open(naam, "r")
    bestand = bestand.readlines()

    return bestand
def getLength(bestand):
    lenghts = []
    for regel in bestand:
        if regel != "CONTIG\n":
            lenghts.append(int(regel))

    return lenghts
def derest(lengtes):
    counter = 0
    seqlength = sorted(lengtes, reverse=True)
    print(seqlength)
    totalScaffold = sum(seqlength)
    N50 = []

    for length in seqlength:
        if sum(N50) < totalScaffold/2:
            N50.append(length)
        else:
            NG50 = N50[-1]
    for lent in seqlength:
        counter += 1
        if NG50 == lent:
            n_N50 = counter
    print(NG50)
    print(numpy.median(seqlength))
    print(numpy.mean(seqlength))

    return totalScaffold, NG50, len(seqlength), numpy.mean(seqlength), seqlength[0], n_N50


def writeFiles(naam, Totaal, N50, n, gem, max, n_N50):
    bestand = open("Assembly.txt", "w")
    bestand.write("$ Assembly of " + naam + "\n")
    bestand.write("Sum = " + str(Totaal) + ", n = " + str(n) + ", average = " + str(gem) + ", max = "  + str(max) + "\n")
    bestand.write("N50 = " + str(N50) + ", n = " + str(n_N50) + "\n")

    return 0


def main():
    naam = "Scaffoldfile.txt"
    bestand = Openen(naam)
    lengtes  =getLength(bestand)
    Totaal, N50, n, gem, max,n_N50 =  derest(lengtes)
    writeFiles(naam, Totaal, N50, n, gem, max,n_N50)

main()