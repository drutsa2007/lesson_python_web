from xml.dom import minidom

xml = open('xml_sample.xml')

doc = minidom.parse(xml)
node = doc.documentElement
books = doc.getElementsByTagName("book")

titles = []
for book in books:
    titleObj = book.getElementsByTagName("title")[0]
    titles.append(titleObj)

for title in titles:
    nodes = title.childNodes
    for node in nodes:
        if node.nodeType == node.TEXT_NODE:
            print(node.data)

