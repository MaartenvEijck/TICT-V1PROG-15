naam = input('Geef je naam op: ')

import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
tijd = vandaag.strftime("%H:%M:%S")


infile = open('Hardlopers.txt', 'a')
infile.write('{}, {}, {}\n'.format(s,tijd,naam))
infile.close()

