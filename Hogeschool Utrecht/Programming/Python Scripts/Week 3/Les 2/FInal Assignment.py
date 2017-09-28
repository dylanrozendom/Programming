def toon_aantal_kluizen_vrij():
    file = open("kluizen.txt", "r")
    regel = len(file.readlines())
    if regel <= 0:
        output = 20
    else:
        output = (20 - regel)
    return output

def nieuw_kluis():
    file = open("kluizen.txt", "r+")
    regel = len(file.readlines())
    if int(toon_aantal_kluizen_vrij()) >= 0:
        nummer  = (regel + 1)
        naam = input('Voer hier je naam in ')
        code = input('voer hier je 4 cijverige code in ')
        file.write(str(nummer) + ' - ' + str(naam) + ' - ' + str(code) + '\n')



def kluis_openen():
    nummer = input('je nummer is ')
    code = input('Je code is ')
    file = open("kluizen.txt", "r")
    gevonden = 'niet gevonden'
    lijn = file.readlines()
    for x in lijn:
        lijst = x.split(' - ')
        if nummer in lijst and code+'\n' in lijst:
            gevonden = 'combinatie is gevonden'
    return gevonden

antwoord = True
while antwoord:
    print ("""
    1.Ik wil weten hoeveel kluizen nog vrij zijn
    2.Ik wil een nieuwe kluis
    3.Ik wil even iets uit mijn kluis halen
    4.Stoppen
    """)
    antwoord=input("Wat wil je doen ")
    if antwoord=="1":
      print(toon_aantal_kluizen_vrij())
    elif antwoord=="2":
      print(nieuw_kluis())
    elif antwoord=="3":
      print(kluis_openen())
    elif antwoord=="4":
      print("\n Stoppen")
      break
    elif antwoord !="":
      print("\n Geen goed antwoord")
