import csv
highscore = ['0','0','0']
with open('gamefile.csv', 'r') as myCSVFile:

    reader = csv.reader(myCSVFile, delimiter=';')
    for row in reader:
        if highscore[2] < row[2]:
            highscore[0] = row[0],row[1],row[2]

print(highscore[0])