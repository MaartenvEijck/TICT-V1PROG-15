def ticker():
    infile = open('Tickersym.txt' , 'r')
    regels = infile.readlines()
    infile.close()
    tickerdict = {}
    for regel in regels:
        tickerregel = regel.split(':')
        sleutel = tickerregel[0]
        waarde = tickerregel[1].split()
        tickerdict[sleutel] = waarde
    return tickerdict

print(ticker())