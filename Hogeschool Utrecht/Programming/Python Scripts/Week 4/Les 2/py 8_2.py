def monopolyworp():
    import random
    test = True
    x = 0
    while test:
        gooione = random.randrange(1, 7)
        gooitwo = random.randrange(1, 7)
        dubbel = gooione + gooitwo
        if gooione == gooitwo:
            print(str(gooione) + ' + ' + str(gooitwo) + ' = ' + str(dubbel) + ' (dubbel)')
            continue
        elif x == 3:
            print(str(gooione) + ' + ' + str(gooitwo) + ' = ' + '(direct naar gevangenis)')
            break
        else:
            print(str(gooione) + ' + ' + str(gooitwo) + ' = ' + str(dubbel))
            break

monopolyworp()