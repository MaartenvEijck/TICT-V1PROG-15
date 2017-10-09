getal = 1
aantal = 0
som = 0
while getal != 0:
   getal = eval(input('Geef een getal op: '))
   aantal += 1
   som =som + getal

print('er zijn {} ingevoerd en de som is {}' .format(aantal-1, som))
