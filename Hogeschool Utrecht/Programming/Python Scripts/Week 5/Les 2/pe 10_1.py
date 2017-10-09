import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

filedict = processXML('newfile.xml')
artikelen = filedict['artikelen']['artikel']

for artikel in artikelen:
    print(artikel['naam'])
