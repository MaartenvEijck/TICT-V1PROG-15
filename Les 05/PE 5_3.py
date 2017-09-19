infile = open('Kaartnummers.txt')
inhoud = infile.readlines()
infile.close()

aantal = len(inhoud)
lst = []
print('In dit bestand staan {} aantal regels'.format(aantal))

for regel in inhoud:#hier zet ik alle kaartnummers in
    deel = regel.split(',')
    lst.append(deel[0])

hoogste = max(lst)
regellijn = lst.index(hoogste) + 1
print('Het hoogste getal is {}, en staat in regel {}'.format(hoogste,regellijn))