import csv

with open('C:/GitHub/python_scripts/transpose/Dow20.csv', 'rb') as csvfile:
	fileReader = csv.reader(csvfile, delimiter=',', quotechar='"')
	fileList = list(fileReader)

i=0
temp=[]
transposedFileList=[]
for row in fileList:
	if row[0]!="":
		temp.append(row)
	else:
		transposedFileList.extend([list(i) for i in zip(*temp)])
		del temp[:]

transposedFileList.extend([list(i) for i in zip(*temp)])

with open('C:/GitHub/python_scripts/transpose/Dow21.csv', 'wb') as myfile:
	wr = csv.writer(myfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	wr.writerows(transposedFileList)
