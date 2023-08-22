import xml.dom.minidom


with open("appt2.xml", "r") as f:
    data = f.read()

dom = xml.dom.minidom.parseString(data)

word = dom.getElementsByTagName('word')[0]
# delete attribute
if word.hasAttribute('rrr'):
    word.removeAttribute('rrr')
# delete parameter
name = word.getElementsByTagName('name')[0]
word.removeChild(name)

with open("appt2.xml", "w") as f:
    f.write(dom.toxml())