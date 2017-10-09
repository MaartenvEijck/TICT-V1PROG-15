import random
def diceprob(invoersom):
    aantalworpinv = 0
    aantalworp = 0
    while aantalworpinv <100:
        aantalogen1 = random.randrange(1, 7)
        aantalogen2 = random.randrange(1, 7)
        som = aantalogen1 + aantalogen2

        if som == invoersom:
            aantalworpinv += 1
        aantalworp += 1
    print('Het aantal benodige worpen is {}'.format(aantalworp))



somaantal = eval(input('Hoe groot is de som: '))
diceprob(somaantal)

