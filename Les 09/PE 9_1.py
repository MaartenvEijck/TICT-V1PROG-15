try:
    bedrag = 4356
    index = int(input("Hoeveel personen gaan er mee: "))
    uitkomst = bedrag/index
    if bedrag < 0:
        print('Het gegeven getal mag niet')
    print("Het bedrag per persoon is €{}". format(uitkomst) )
except ValueError:
    print("Het moet een geheel getal zijn")
except ZeroDivisionError:
    print('Je kan niet met minder dan 1 man gaan')
except TypeError:
    print("De list bevat een niet numeriek element")
