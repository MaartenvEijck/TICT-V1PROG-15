pets = ['boa','cat', 'dog']
for pet in pets:
    print(pet)

for pet in pets:
    print(pet, end=', ')

woord = 'eenHeelErgLangWoord'
for letter in woord:
    print(letter, end =' ')

naam = 'Mark Rutte'
plaats = 'Den Haag'

print('Mijn naam is ' + naam + 'en ik woon in ' + plaats)
print('Mijn naam is {} en ik woon in {} ' .format(naam,plaats))

leeftijd1 = 17
leeftijd2 = 18
som = leeftijd1 + leeftijd2
print('De som van de leeftijden is ' + str(som))
print('De som van de leeftijden is {}' .format(som))