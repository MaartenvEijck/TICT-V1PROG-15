import datetime
import csv

with open('inloggers.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    while True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde' or naam == 'Einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        writer.writerow((voorl,naam,gbdatum,email))






bestand = 'inloggers.csv'

