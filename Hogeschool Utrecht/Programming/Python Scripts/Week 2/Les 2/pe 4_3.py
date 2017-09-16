lengte = eval(input('lengte gebruiker'))

def lang_genoeg(pizza):
    if pizza > 120:
        return ("gefeliciteerd je mag erin")
    else:
       return ("mag niet")

print(lang_genoeg(lengte))
