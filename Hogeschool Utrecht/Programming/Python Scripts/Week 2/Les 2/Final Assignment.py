def standaardprijs(afstandKM):
    if afstandKM <= 50:
        return(afstandKM * 0.80)
    else:
        return(15 + (afstandKM * 0.60))

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)

    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit:
            return prijs * 0.65
        else:
            return prijs * 0.70
    else:
        if weekendrit:
            return prijs * 0.60
        else:
            return prijs

afstandKM = 100
Leeftijd = 65
weekendrit = False

print(ritprijs(Leeftijd,weekendrit,afstandKM))

