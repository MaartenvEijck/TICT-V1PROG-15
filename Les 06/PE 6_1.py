def seizoen(maand):
    if maand >=3 and maand <=5:
        return('Lente')
    elif maand >=6 and maand <=8:
        return ('Het is zomer')
    elif maand >=9 and maand <=11:
        return ('Het is herfst')
    else:
        return ('Het is winter')

maandnummer = eval(input('Wat is het nummer van de maand? '))
print(seizoen(maandnummer))

