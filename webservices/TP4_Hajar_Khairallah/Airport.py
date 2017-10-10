from zeep import Client
import xml.etree.ElementTree as ET

webservice="http://www.webservicex.net/airport.asmx?WSDL"
client=Client(webservice)
result=client.service.getAirportInformationByAirportCode('YQB')
root = ET.fromstring(result)

for child in root.iter('CityOrAirportName'):
    print(child.text)


