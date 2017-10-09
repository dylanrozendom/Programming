import csv

with open('Artikel.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')
    for row in reader:

