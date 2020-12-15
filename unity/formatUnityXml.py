import sys
import xml.dom.minidom

s=sys.stdin.read()
xmlData = xml.dom.minidom.parseString(s)
dicts = xmlData.getElementsByTagName('dict')
parent = None
for dict in dicts:
    parent = dict.parentNode
    parent.removeChild(dict)

dicts[:] = sorted(dicts, key=lambda dict: (dict.childNodes[0].nodeValue, dict.childNodes[2].firstChild.nodeValue, dict.childNodes[1].firstChild.nodeValue))

for dict in dicts:
    parent.appendChild(dict)
    # [<DOM Comment node "u' Realtime '...">, <DOM Element: key at 0x10c163758>, <DOM Element: string at 0x10c163830>]

print(xmlData.toprettyxml())
