invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst = invoer.split('-')
gesorteerd = sorted(lijst)
som = sum(int(i) for i in gesorteerd)
lengte = (len(lijst))
print(gesorteerd)
Gemiddelde = som / lengte

print("Grootste getal: " + max(lijst) + " en Kleinste getal: " + min(lijst))
print('Aantal getallen: ' + str(len(lijst)) + " en Som van getallen: " + str(som))
print('Gemiddelde: ' + str(Gemiddelde))