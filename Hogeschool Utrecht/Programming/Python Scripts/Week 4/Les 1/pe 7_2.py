test = True
while test:
    letters = input("Geef een string van vier letters: ")
    if len(letters) is not 4:
        print(letters + ' heeft ' + str(len(letters)) + ' letters ')
    else:
        print('Inlezen van het correcte string: ' + str(letters) + ' is geslaagd')
