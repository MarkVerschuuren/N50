bestand = open("predictions2.fa", "r")
regel = bestand.readline()



count = 0
value = True
counter = 0
while value == True:
    if regel == "":
        value = False
    if "DOC_50" in regel:
        counter += 1
        regel = bestand.readline()
        while ">" not in regel:

            count += len(regel)
            regel = bestand.readline()
        print("DOC_50_" + str(counter) + " Len : " + str(count) + "\n")
    regel = bestand.readline()


print(counter)