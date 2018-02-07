import re

lines = ["Bio-informatica studenten van"
    , "de Hogeschool van Arnhem en Nijmegen"
    , "blijken zeer gewilde stagiaires te zijn"
    , "Dat komt onder andere doordat zij zeer"
    , "bedreven zijn in het schrijven van"
    , "Regular Expressions"]

for line in lines:
    if re.search("^[A-Z]", line):
        print(re.search("^[A-Z]", line))
        print(line)