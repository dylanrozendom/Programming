def seizoen(maand):
    if maand in range(3,5):
        return ('het is lente')
    elif maand in range(6,8):
        return ('het is zomer')
    elif maand in range(9,11):
        return ('het is herfst')
    elif maand in (12,1,2):
        return ('het is winter')
    return

print(seizoen(12))