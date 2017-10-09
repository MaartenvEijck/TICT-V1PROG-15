try:
    numlist = [100,101,0,'103', 104]
    index = int(input('Geef een index: '))
    print(100/numlist[index])
except ValueError:
    print('Je moet een geheel getal invoeren')
except ZeroDivisionError:
    print('De list bevat een 0')
except TypeError:
    print('De list bevat een niet numeriek element')
except IndexError:
    print('Je moet een getal tussen -5 en 4 invoeren')

