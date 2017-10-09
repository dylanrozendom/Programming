stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel','Utrecht Centraal','s-Hertogenbosch','Eindhoven','Weert','Roermond','Sittard','Maastricht']

def inlezen_beginstation(stations):
    while True:
        beginstation = input('Wat is je beginstation? ').capitalize()
        if beginstation in stations:
            return beginstation
        elif beginstation not in stations:
            print('Deze trein komt niet in ' + str(beginstation))

def inlezen_eindstation(stations, beginstation):
    loop = True
    while loop:
        eindstation = input('Wat is je eindstation? ').capitalize()
        begin = stations.index(beginstation)
        eind = stations.index(eindstation)
        if eindstation in stations and begin < eind:
            return eindstation
        else:
            print('Niet het juiste traject ' + str(eindstation))

def omroepen_reis(stations, beginstation, eindstation):
    afstand = stations.index(eindstation) - stations.index(beginstation)
    begin = stations.index(beginstation) + 1
    eind = stations.index(eindstation) + 1
    euro = afstand * 5
    print('Het begin station ' + str(beginstation) + ' is het ' + str(begin) + 'e' + ' station in het traject')
    print('Het begin station ' + str(eindstation) + ' is het ' + str(eind) + 'e' + ' station in het traject')
    print('De afstand bedraagt ' + str(afstand) + ' stations')
    print('De prijs van het kaartje is ' + str(euro) + ' euro')
    print('')
    print('jij stapt in de trein in ' + str(beginstation) + ' - ')
    print('jij stapt uit in ' + str(eindstation))

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
