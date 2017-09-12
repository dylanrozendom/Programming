age = eval(input("leeftijd: "))
paspoort = input("Nederlands paspoort: ")


if age > 17 and paspoort == 'ja' :
    print ("Gefeliciteerd je mag stemmen")
else:
    print ("je mag niet stemmen")