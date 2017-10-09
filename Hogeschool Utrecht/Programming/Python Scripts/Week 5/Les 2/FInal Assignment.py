import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

filedict = processXML('stations.xml')
stations = filedict['Stations']['Station']

print('Dit zijn de codes en types van de 4 stations: ')
for station in stations:
    print(station['Code'] + ' - ' + station['Type'])

print('\n')
for station in stations:
    if station['Synoniemen'] != None:
        print (station['Code'], ' - ',station['Synoniemen'])

print('\n')
print('Dit zijn de lange naam van elk station')
for station in stations:
    print(station['Code'] + ' - ' + station['Namen']['Lang'])