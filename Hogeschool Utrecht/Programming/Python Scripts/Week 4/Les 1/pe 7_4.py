def ticker(filename):
    bedrijf = input('Enter Company name: ')
    directory = {}
    filehandle = open(filename)
    for line in filehandle:
        (key, val) = line.split(':')
        directory[key] = val.rstrip()
    for key,val in directory.items():
        if key == bedrijf:
            return 'Ticker Symbol ' + val
        elif val == bedrijf:
            return 'Company name: ' + key


print(ticker('namen.txt'))