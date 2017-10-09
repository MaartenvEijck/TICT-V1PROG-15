def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt')
    lst = infile.readlines()
    ingebruik = len(lst)
    over = 12 - ingebruik
    infile.close()
    print("er zijn nog {} kluizen beschikbaar\n".format(over))

def nieuwe_kluis():
    kluisnummers = [1,2,3,4,5,6,7,8,9,10,11,12]
    infile = open('kluizen.txt')
    regelslezen = infile.readlines()
    for regel in regelslezen:
        regelsplit = regel.split(';')
        kluisnummer = int(regelsplit[0])
        if kluisnummer in kluisnummers:
            kluisnummers.remove(kluisnummer)

    if len(kluisnummers) != 0:
        wachtwoord = input('Typ hier de kluiscode voor uw kluis in: ')
        if len(wachtwoord) < 4:
            print('Uw wachtwoord is te kort, deze moet minimaal 4 tekens lang zijn!')
        else:
            outfile = open ('kluizen.txt', 'a')
            outfile.write('{};{}\n'.format(kluisnummers[0],wachtwoord))
            print('Uw heeft kluisnummer: {}'.format(kluisnummers[0]))
            outfile.close()
    else:
        print('Er zijn geen kluizen meer beschikbaar.')
    infile.close

def kluis_openen():
    kluisnummer = input('Wat is uw kluisnummer: ')
    wachtwoord = input('Geef uw wachtwoord op: ')
    checker = '{};{}'.format(kluisnummer, wachtwoord)
    infile = open('kluizen.txt', 'r')
    combinaties = infile.readlines()
    infile.close()
    goed = False
    for combo in combinaties:
        if checker in combo:
         print('U heeft de goede code ingevoerd.')
         goed = True
         break
        else:
            goed = False
    if goed == False:
        print('De combinatie van kluisnummer en code is onjuist.')

print('1: Ik wil weten hoeveel kluizen er nog beschikbaar zijn \n2: Ik wil een nieuwe kluis\n3: Ik wil iets uit mijn kluis halen')
menukeuze = input('\nWelke optie wilt u gebruik van maken? ')
if menukeuze not in '123':
    print('Dit is geen optie')
else:
    intmenukeuze = int(menukeuze)
    if intmenukeuze ==1:
        toon_aantal_kluizen_vrij()
    elif intmenukeuze ==2:
        nieuwe_kluis()
    elif intmenukeuze ==3:
        kluis_openen()
    else:
        print('Dit is geen optie')