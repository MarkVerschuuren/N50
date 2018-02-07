def Openen():
    try:
        bestand = open("Debaryomyces_occidentalis.fas")
        bestand = bestand.readlines()

        return bestand
    except IOError:
        print("IOError oh no!")


def getLength(bestand):
    lengths = []
    seq = ""

    for regel in bestand:
        print(regel)
        if ">" not in regel:
            seq += regel
        else:
            if len(seq) > 0:
                lengths.append(len(seq))
                seq = ""



    return lengths
def writeFile(lengths):
    writebestand = open("Scaffoldfile.txt", "w")
    writebestand.write("CONTIG" + "\n")
    for length in lengths:
        writebestand.write(str(length) + "\n")








def main():
    bestand = Openen()
    lengths = getLength(bestand)
    writeFile(lengths)
main()