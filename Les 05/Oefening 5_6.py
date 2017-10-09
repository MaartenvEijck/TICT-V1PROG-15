infile = open('kaartnummers.txt', 'r')
outfile = open('oefening 5_6.txt', 'r')
outfile.close()
inhoud = infile.readlines()
infile.close()
for onderdeel in inhoud:
    lijst1 = onderdeel.split(',')
    print('{} heeft kaartnummer: {}'.format(lijst1[1].strip(), lijst1[0].strip()))