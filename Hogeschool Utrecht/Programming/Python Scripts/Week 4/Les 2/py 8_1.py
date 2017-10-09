groen = {'beukenlaan','geldrop','heeze','weert','best'}
bruin = {'best','helmond hout', 'helmond', 'helmond brouwhuis', 'deurne','beukenlaan'}
trajecten = groen.union(bruin)
print (groen.intersection(bruin))
print (groen.difference(bruin))
print (bruin.difference(groen))
print (trajecten)