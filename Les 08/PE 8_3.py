def code(invoerstring):
    nieuwwoord = ''
    for letter in invoerstring:
        getalnieuweletter = ord(letter) + 3
        nieuwletter = chr(getalnieuweletter)
        nieuwwoord = nieuwwoord + nieuwletter
    print('De uitvoer van de nieuwe zin wordt: {}'.format(nieuwwoord))

invoerstring = input('Geef uw wachtwoord: ')
code(invoerstring)