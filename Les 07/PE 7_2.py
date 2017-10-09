lengte = 0

while lengte != 4:
    woord = input('Geef een woord: ')
    lengte = len(woord)
    if lengte == 4:
        print('inlezen van correcte string: {} is geslaagd.'.format(woord))
        break
    else:
        print('{} heeft {} letters.'.format(woord,lengte))