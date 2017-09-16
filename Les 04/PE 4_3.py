def lang_genoeg(lengte):
    if lengte >= 120:
        return ('Je bent lang genoeg voor de attractie!')
    else:
        return ('Sorry, je bent te klein!')

lengte = eval(input('Lengte in centimeters:  '))
print(lang_genoeg(lengte))