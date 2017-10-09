import csv
with open('artikel.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')
    duursteartikel = 0
    for row in reader:
        prijs = float(row['Prijs'])
        if prijs > duursteartikel:
            duursteartikel = prijs
            duurste_naam = row['Naam']
    print(duursteartikel, duurste_naam)