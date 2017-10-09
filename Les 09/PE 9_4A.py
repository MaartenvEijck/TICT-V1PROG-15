import csv

with open('artikel.csv', 'w', newline='')as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('artikelnummer','artikelcode', 'naam', 'voorraad', 'prijs'))
    while True:
        artikelnummer = input('Geef het artikelnummer op: ')
        if artikelnummer == '':
            break
        artikelcode = print('Geef artikelcode op: ')
        naam = print('Geef de naam op: ')
        voorraad = print('Geef de voorraad op: ')
        prijs = print('Geef de prijs op: ')
        writer.writerow((artikelnummer, artikelcode, naam, voorraad, prijs))
