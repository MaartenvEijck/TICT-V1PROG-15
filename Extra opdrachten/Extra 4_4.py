bedrag = eval(input('Welk bedrag heeft u: '))
rente = eval(input('Wat is het rentepercentage: '))

def eindbedrag(bedrag, rente):
    bedrag = bedrag + (rente * bedrag / 100)
    return bedrag
print(eindbedrag(bedrag, rente))
