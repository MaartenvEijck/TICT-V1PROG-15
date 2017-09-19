infile = open('kaartnummers.txt', 'r')
inhoud = infile.readlines()
infile.close()
for onderdeel in inhoud:
    lijst1 = onderdeel.split(',')
    print('{} heeft kaartnummer: {}'.format(lijst1[1].strip(), lijst1[0].strip()))