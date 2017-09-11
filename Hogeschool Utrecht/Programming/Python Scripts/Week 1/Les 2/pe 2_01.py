letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
alphabet = ['A', 'B', 'C', 'D']
legelijst = []

for letter in alphabet:
    if letters.count(letter):
        legelijst.append(letter + " : " + str(letters.count(letter)))

print(legelijst)
