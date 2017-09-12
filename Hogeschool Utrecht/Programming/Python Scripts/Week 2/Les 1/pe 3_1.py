score = eval(input("Geef je score:" + " "))
totaal = score > 15

if totaal:
    print ("Gefeliciteerd")
    print ("Met een score van" + " " + str(score) + "ben je geslaagd!")
else:
    print ("Niet geslaagd")