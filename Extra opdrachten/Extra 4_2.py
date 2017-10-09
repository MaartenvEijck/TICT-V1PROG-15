temp = eval(input('Wat is de temperatuur vandaag: '))

def geefmelding(temp):
    if temp < 0:
        print ('Het vriest vandaag.')
    elif temp >= 0 and temp <=15:
        print('Het is koud vandaag')
    else:
        print('Het is lekker weer vandaag.')
print(geefmelding(temp))