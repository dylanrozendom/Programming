from time import strftime
file = open('Hardlopers.txt', 'w')
time = strftime("%a" + ' ' + "%d" + ' ' + '%b' + " " + "%X")

while True:
    if True:
        file = open("hardlopers.txt", "a")
        naam = input("naam: ")
        file.write(str(time) + " " + str(naam) + "\n")
        file.close()
    else:
        break