def kwadraten_som(grondgetallen):
    lijst1 = []
    for c in grondgetallen:
        if c >= 0:
            kwadraat = c * c
            lijst1.append(kwadraat)
            b = sum(lijst1)
    return(b)


print(kwadraten_som([4, 5, 3, -81]))


