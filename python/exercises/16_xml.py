import xml.dom.minidom as md


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

f = md.parse("sample.xml")
books = f.getElementsByTagName("book")

for book in books:
    print(getText(book.getElementsByTagName("price")[0].childNodes))


# increase price of all books 10x
for book in books:
    priceNode = book.getElementsByTagName("price")[0].childNodes[0]
    priceNode.nodeValue = str(10*float(priceNode.nodeValue))

with open("sample.out.xml", "w") as fs:
    fs.write(f.toxml())
