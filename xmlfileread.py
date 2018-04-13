from xml.dom.minidom import parse
import xml.dom.minidom
import csv

def xmlfile():
	DOMTree = xml.dom.minidom.parse("etlproject1.xml")
	collection = DOMTree.documentElement
	if collection.hasAttribute("shelf"):
   		print "Root element : %s" % collection.getAttribute("shelf")
	rows = collection.getElementsByTagName("Row")

	for row in rows:
		cells = row.getElementsByTagName("Cell")
		for cell in cells:
			data1 = cell.getElementsByTagName('Data')[0]
			print "%s " % data1.childNodes[0].data,
		print ""

def xmlfiletransform():
	DOMTree = xml.dom.minidom.parse("etlproject1.xml")
	collection = DOMTree.documentElement
	if collection.hasAttribute("shelf"):
		print "Root element : %s" % collection.getAttribute("shelf")
	rowkeys = collection.getElementsByTagName("Row")
	rows=[]
	for row in rowkeys:
		x=[]
		cells = row.getElementsByTagName("Cell")
		for cell in cells:
			data1 = cell.getElementsByTagName('Data')[0]
			y=data1.childNodes[0].data
			x.append(y)
		rows.append(x)
	for row in rows:
		temp=row[2]
		var=temp[8:10]+temp[4]+temp[5:7]+temp[4]+temp[2:4]
		row[2]=var
		temp=row[3]
		if(int(temp)>1000000):
			row[3]='A'
		else:
			row[3]='B'
		temp=row[4]
		if(temp=='Female' or temp=='FEMALE'):
			row[4]='F'
		else:
			row[4]='M'
	for row in rows:
		for col in row:
			print("%10s"%col),
		print('\n')

def xmlfileload():
	DOMTree = xml.dom.minidom.parse("etlproject1.xml")
	collection = DOMTree.documentElement
	if collection.hasAttribute("shelf"):
		print "Root element : %s" % collection.getAttribute("shelf")
	rowkeys = collection.getElementsByTagName("Row")
	rows=[]
	for row in rowkeys:
		x=[]
		cells = row.getElementsByTagName("Cell")
		for cell in cells:
			data1 = cell.getElementsByTagName('Data')[0]
			y=data1.childNodes[0].data
			x.append(y)
		rows.append(x)
	for row in rows:
		temp=row[2]
		var=temp[8:10]+temp[4]+temp[5:7]+temp[4]+temp[2:4]
		row[2]=var
		temp=row[3]
		if(int(temp)>1000000):
			row[3]='A'
		else:
			row[3]='B'
		temp=row[4]
		if(temp=='Female' or temp=='FEMALE'):
			row[4]='F'
		else:
			row[4]='M'
	filename2 = "etlfinal.csv"
	with open(filename2, 'ab') as f:
		csvwriter = csv.writer(f)
		csvwriter.writerows(rows)
	f.close()