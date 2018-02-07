import re

bestand = open("prots (1).fa.txt")
bestand  = bestand.readlines()

value = ""
key = ""
count = 0
dictt = {}
for regel in bestand:
    if ">" not in regel:
        value += regel
    elif count > 0 and ">" in regel:
        dictt[key] = value
        key = ""
        value = ""

    if ">" in regel:
        count += 1
        key = regel
dictt[key] = value

for key, value in dictt.items():
    if re.findall("C.C.{3,5}C.{7}G.C.{9}CC", value):
        print("Matcch")
