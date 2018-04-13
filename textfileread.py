import csv
def textfile():
	file=open("etlproject3.txt","r")
	print file.read()


def textfiletransform():
	file=open("etlproject3.txt","r")
	data=file.read().splitlines()
	rows=[]
	for x in data:
		y=x.split()
		rows.append(y)
	for row in rows:
		temp=row[2]
		var=temp[3:5]+temp[2]+temp[0:2]+temp[2]+temp[-2:]
		row[2]=var
		temp=row[3]
		if(int(temp)>1000000):
			row[3]='A'
		else:
			row[3]='B'
		temp=row[4]
		if(temp=='female'):
			row[4]='F'
		else:
			row[4]='M'
	for row in rows:
		for col in row:
			print("%10s"%col),
		print('\n')

def textfileload():
	file=open("etlproject3.txt","r")
	data=file.read().splitlines()
	rows=[]
	for x in data:
		y=x.split()
		rows.append(y)
	for row in rows:
		temp=row[2]
		var=temp[3:5]+temp[2]+temp[0:2]+temp[2]+temp[-2:]
		row[2]=var
		temp=row[3]
		if(int(temp)>1000000):
			row[3]='A'
		else:
			row[3]='B'
		temp=row[4]
		if(temp=='female'):
			row[4]='F'
		else:
			row[4]='M'
	filename2 = "etlfinal.csv"
	with open(filename2, 'ab') as f:
		csvwriter = csv.writer(f)
		csvwriter.writerows(rows)
	f.close()