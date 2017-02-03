import csv

with open('C:/GitHub/python_scripts/transpose/Dow.csv', 'r') as infile:
    readie = csv.reader(infile, delimiter=',', quotechar='"')
    with open('C:/GitHub/python_scripts/transpose/Dow20.csv', 'wb') as output:
        outwriter=csv.writer(output, delimiter=',')
        i = 0
        for row in readie:
             outwriter.writerow(row)
             i += 1
             if i % 17 == 0:
                 # write the empty row
                 outwriter.writerow([])