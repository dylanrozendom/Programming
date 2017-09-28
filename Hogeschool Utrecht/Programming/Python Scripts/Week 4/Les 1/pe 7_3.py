cijfers = {'Melinda':6, 'Louis':5, 'Rudolph':7, 'Mercedes':8, 'Jeremy':9, 'Julia':10, 'Colleen':5}
test = 0

for naam,cijfer in cijfers.items():
    if cijfer >= 9:
        print('naam ' + naam + ' cijfer: ' + str(cijfer))