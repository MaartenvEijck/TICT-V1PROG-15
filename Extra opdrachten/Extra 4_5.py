getallenrij = [23,35,31,26,73,75,84,29,42,46]

def berekensomevengetallen(getallenrij):
    som = 0
    for getal in getallenrij:
        if getal %2 == 0:
            som = som + getal
    print('De som is {}'.format(som))
berekensomevengetallen(getallenrij)