def Openen():
    bestand = open("augustus.gff", "r")

    return bestand

def leesBestand(bestand):
    value = True
    schrijfbestand = open("predictions2.fa", "w")
    while value == True:
        seq = ""
        regel = bestand.readline()
        if regel == "":
            value = False
        elif "# start" in regel:
            regel = bestand.readline()
            regel = regel.split()
            schrijfbestand.write(">" + regel[0] + "| Start - " + regel[3] +"| Stop - " + regel[4] + "|\n" )
        elif "# protein" in regel:
            while "# end gene" not in regel:
                seq += regel
                regel = bestand.readline()
            seq = seq.replace("#","")
            seq = seq.split("[")[1].replace("]","").replace(" ","")
            schrijfbestand.write(seq + "\n")

def main():
    bestand  = Openen()
    leesBestand(bestand)
main()