from time import strftime
import csv



with open('newfile.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('naam', 'voorl', 'gbdatum', 'email'))
    time = strftime("%a" + ' ' + "%d" + ' ' + '%b' + " " + "%X")
    while True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")

        writer.writerow((time,naam, voorl,gbdatum,email))

