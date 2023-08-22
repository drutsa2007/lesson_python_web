import xml.dom.minidom


with open("xml_sample.xml", "r") as f:
    data = f.read()

dom = xml.dom.minidom.parseString(data)

folder = dom.getElementsByTagName('name')[0]
folder.setAttribute("is_acronym", "False")
folder.childNodes[0] = dom.createTextNode("dfsdf")

with open("appt2.xml", "w") as f:
    f.write(dom.toprettyxml())