def code(invoerstring):
    lijst = []
    for x in invoerstring:
        test = ord(x) + 3
        testnew = chr(test)
        lijst.append(testnew)
    str1 = ''.join(lijst)
    print(str1)
code('RutteAlkmaarDen Helder')