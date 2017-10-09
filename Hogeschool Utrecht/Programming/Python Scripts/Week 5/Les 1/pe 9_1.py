kosten = 4356
try:
    a = eval(input('Met Hoeveel mensen ga je op vakantie '))
    eind = kosten / a
    if a < 0:
        print('Mag niet negatief zijn')
    else:
        print (eind)

except ZeroDivisionError:
    print('Delen door nul kan niet!')

except NameError:
    print('Gebruik cijfers voor het invoeren van het aantal')

except Exception:
    print('Onjuiste invoer')