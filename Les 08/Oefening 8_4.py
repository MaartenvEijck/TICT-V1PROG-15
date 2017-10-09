invoer = input('Geef een woord op: ')

for karakter in invoer:
    asc = ord(karakter)
    print('{} {} {:x} {:b}'.format(karakter,asc,asc,asc))