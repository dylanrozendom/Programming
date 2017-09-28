input = eval(input('Geef lijst met minimaal 10 strings: '))
nieuwlijst = []

for woord in input:
    if len(woord) == 4:
        nieuwlijst.append(woord)


print(nieuwlijst)