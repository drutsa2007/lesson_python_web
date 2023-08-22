import xml.dom.minidom

doc = xml.dom.minidom.parseString("<dictionary/>")
root = doc.documentElement

word = doc.createElement("word")

root.appendChild(word)

first = doc.createElement("update")
first.setAttribute("date", "2100-01-01")

word.appendChild(first)

second = doc.createElement("name")
second.setAttribute("is_acronym", "true")
text = doc.createTextNode("DTD")
second.appendChild(text)
word.appendChild(second)

third = doc.createElement("definition")
third.appendChild(doc.createTextNode("Document Type Definition"))
word.appendChild(third)

with open("appt.xml", "w") as f:
    f.write(doc.toprettyxml())