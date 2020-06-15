inport urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url=input("Enter the location")
a=urllib.urlopen(url)
data=a.read()
print('length of data is'len(data))
print(data.decode())

tree=ET.fromstring(data)
s=tree.findall('comments').text
print(len(s))
        for i in s:
            counts=i.findall('.//count')
print(counts)            
