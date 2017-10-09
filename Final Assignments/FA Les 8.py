stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", "Eindhoven", 'Weert', 'Roermond', 'Sittard', 'Maastricht' ]

def inlezen_beginstation(stations):
    beginstation = input('Geef het beginstation: ')
    while beginstation not in stations:
        beginstation = input('Geef een nieuw beginstation op: ')
    return beginstation

def inlezen_eindstation(stations,beginstation):
    eindstation = input('Geef het eindstation op: ')
    while eindstation not in stations:
        eindstation = input('Geef een nieuw eindstation op: ')
    while stations.index(eindstation)<= stations.index(beginstation):
        eidnstation = input('Geef nieuw eindstation op: ')
    return eindstation

def omroepen_reis(station, beginstation, eindstation):
    nummerB = stations.index(beginstation) + 1
    nummerE = stations.index(eindstation) + 1
    print('Het beginstation {} is het {}e station in het traject '.format(beginstation, nummerB))
    print('Het eindstation {} is het {}e station in het traject'.format(eindstation, nummerE))
    afstand = nummerE - nummerB
    prijs = 5*afstand
    print('De prijs is {}'.format(prijs))
    print('Je stapt in bij {}'.format(beginstation))
    for i in range (nummerB, nummerE -1):
        print('-'+station[i])
    print('Je stapt uit bij {}'.format(eindstation))

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)