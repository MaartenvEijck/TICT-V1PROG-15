lengte = eval(input('Geef je lengte: '))
gewicht = eval(input('Geef je gewicht: '))
bmi = gewicht/(lengte/100)**2

if bmi <18.5:
    print('Je hebt ondergewicht')
elif bmi >=18.5 or bmi <= 25:
    print('normaal')
else:
    print('overgewicht')