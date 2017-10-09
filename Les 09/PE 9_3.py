import csv
with open('gamers.csv','r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    hoogstescore = 0
    for row in reader:
        score = int(row[2])
        if score > hoogstescore:
            hoogstescore = score
            hoogstenaam = row[0]
            hoogstedatum = row[1]
    print('De hoogste score is: {} op {} gehaald door {}'.format(hoogstescore,hoogstedatum, hoogstenaam))