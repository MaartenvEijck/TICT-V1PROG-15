def monopolyworp():
    dubbel =0
    import random

    while dubbel <2:
        steen1 = random.randrange(1,7)
        steen2 = random.randrange(1,7)
        totaal = steen1 + steen2
        if steen1 == steen2:
            print('{} + {} = {} dubbel'.format(steen1,steen2,totaal))
            dubbel +=1
        else:
            print('{} + {} = {}'.format(steen1,steen2,totaal))
            break
    if dubbel ==2:
        print('{} + {} = ga direct naar de gevangenis'.format(steen1,steen2))
while True:
    monopolyworp()