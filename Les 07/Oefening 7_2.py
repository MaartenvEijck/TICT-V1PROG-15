week = {'ma': 'maandag', 'di': 'dindag', 'wo': 'woensdag', 'do': 'donderdag', 'vr': 'vrijdag'}
print(week['ma'])
week['di'] = 'dinsdag'
week['za'] = 'zaterdag'
for afkorting in week.keys():
    print(afkorting)
print()
for langenaam in week.values():
    print(langenaam)
print()
for beide in week.items():
    print (beide)
print()
for afkorting in week.keys():
    print(afkorting,week[afkorting])
print()
