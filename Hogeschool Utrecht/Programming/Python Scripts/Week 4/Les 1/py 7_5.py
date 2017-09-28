def namen():
    d = {}
    count = 0
    naam = input("Volgende naam ")
    while naam != '':
        if naam in d:
            d[naam] = d[naam] + 1
        else:
            d[naam] = 1
        count = count + 1
        naam = input("Volgende naam ")

    for key,value in d.items():
        if value == 1:
            print('Er is '+ str(value) + ' student met de naam ' + key)
        else:
            print('Er zijn '+ str(value) + ' studenten met de naam ' + key)

namen()