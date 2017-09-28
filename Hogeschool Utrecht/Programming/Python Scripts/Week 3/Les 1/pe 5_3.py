file = open('kaartnummers.txt')
lijst = []
for f in file:
    format = (f[0:6])
    lijst.append(format)
    number = len(lijst)

maximum = max(lijst)
lines = sum(1 for line in open('kaartnummers.txt'))
regel = lijst.index(max(lijst)) + 1

print("Deze file telt" + ' ' + str(lines) + ' ' + "regels")
print("Het grootste kaartnummer is:" + maximum + " " + "en dat staat op regel" + " " + str(regel))