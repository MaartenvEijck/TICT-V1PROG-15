def standaardprijs(afstandKM):
    if afstandKM >0 and afstandKM <= 50:
        prijskaartje = afstandKM * 0.80
    if afstandKM >50:
        prijskaartje = afstandKM * 0.60 + 15
    if afstandKM <= 0:
        prijskaartje = 0
    return (prijskaartje)

def ritprijs(leeftijd, weekendrit, afstandKM):
    if (leeftijd <12 or leeftijd >= 65) and weekendrit == True:
        prijs = standaardprijs(afstandKM) * 0.65
        return (round(prijs, 2))
    if (leeftijd <12 or leeftijd >=65) and weekendrit == False:
        prijs = standaardprijs(afstandKM)* 0.70
        return (round(prijs, 2))
    if (leeftijd >=12 or leeftijd <65) and weekendrit == True:
        prijs = standaardprijs(afstandKM) * 0.60
        return (round(prijs, 2))
    else:
        prijs = standaardprijs(afstandKM)
        return (round(prijs,2))


afstandKM = eval(input('Hoeveel kilometer moet u reizen: '))
weekendrit_input = input('Reist u in het weekend: ')
if weekendrit_input == 'Ja' and weekendrit_input == 'ja':
    weekendrit = True
elif weekendrit_input == 'nee' or weekendrit_input == 'Nee':
    weekendrit = False
leeftijd = eval(input("Wat is uw leeftijd: "))
print('Uw kaartje kost ' , ritprijs(leeftijd,weekendrit,afstandKM) , ' euro.')

print('positieve afstanden <50km:')
print(ritprijs(64, False, 10))  # overig doordeweeks (uitkomst is 8)
print(ritprijs(11, False, 10))  # kinderen doordeweeks(uitkomst is 5.6)
print(ritprijs(12, False, 10))  # overig doordeweeks (uitkomst is 8)
print(ritprijs(65, False, 10))  # ouderen doordeweeks (uitkomst is 5.6)
print(ritprijs(11, True, 10))  # kinderen weeekend(uitkomst is 5.2 )
print(ritprijs(12, True, 10))  # overig weekend (uitkomst is 4.8)
print(ritprijs(64, True, 10))  # overig weekend (uitkomst is 4.8)
print(ritprijs(65, True, 10))  # ouderen weekend(uitkomst is 5.2 )

# positieve afstanden >50km
print('positieve afstanden >50km:')
print(ritprijs(64, False, 60))  # afstand groter dan 50km dus 15€+60*0.6 (uitkoms is 51)
print(ritprijs(11, False, 60))  # afstand groter dan 50km voor kinderen(uitkomst is 35.7)
print(ritprijs(12, False, 60))  # afstand groter dan 50km overig (uitkomst is 51)
print(ritprijs(65, False, 60))  # afstand groter dan 50km voor ouderen(uitkomst is 35.7)
print(ritprijs(11, True, 60))  # afstand groter dan 50km voor kinderen in het weekend(uitkomst is 33.15)
print(ritprijs(12, True, 60))  # afstand groter dan 50km overig in het weekend overig (uitkomst is 30.6)
print(ritprijs(64, True, 60))  # afstand groter dan 50km overig in het weekend(uitkomst is 30.6)
print(ritprijs(65, True, 60))  # afstand groter dan 50km voor ouderen in het weekend (uitkomst is 33.15)

# negatieve afstanden:
print('negatieve afstanden: ')
print(ritprijs(64, False, -10))  # negatieve afstand overig (uitkomst is 0)
print(ritprijs(11, False, -10))  # negatieve afstand kinderen (uitkomst is 0)
print(ritprijs(12, False, -10))  # negatieve afstand overig (uitkomst is 0 )
print(ritprijs(65, False, -10))  # negatieve afstand ouderen(uitkomst is 0)
print(ritprijs(11, True, -10))  # negatieve afstand kinderen in het weekend (uitkomst is 0)
print(ritprijs(12, True, -10))  # negatieve afstand overig in het weekend(uitomst is0)
print(ritprijs(64, True, -10))  # negatieve afstand overig in het weekend (uitkomst is 0)
print(ritprijs(65, True, -10))  # negatieve afstand ouderen in heet weekend (uitkomst is 0)
