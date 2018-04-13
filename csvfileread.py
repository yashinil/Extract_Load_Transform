import csv 
def csvfile():
    filename = "etlproject2.csv"
    fields = []
    rows = []
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.next()
        for row in csvreader:
            rows.append(row)
    print('Field names are:' + ', '.join(field for field in fields))
    for row in rows:
        for col in row:
            print("%10s"%col),
        print('\n')

def csvfiletransform():
    filename1 = "etlproject2.csv"
    fields = []
    rows = []
    with open(filename1, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.next()
        for row in csvreader:
            rows.append(row)
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
        if(temp=='Female' or temp=='FEMALE'):
            row[4]='F'
        else:
            row[4]='M'
    for row in rows:
        for col in row:
            print("%10s"%col),
        print('\n')

def csvfileload():
    filename1 = "etlproject2.csv"
    filename2 = "etlfinal.csv"
    fields = []
    rows = []
    with open(filename1, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.next()
        for row in csvreader:
            rows.append(row)
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
        if(temp=='Female' or temp=='FEMALE'):
            row[4]='F'
        else:
            row[4]='M'
    with open(filename2, 'ab') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(rows)
    f.close()