weekdag = 'dinsdag'
dag = 25
maand = 'maart'
uur = 14
minuten = 15
print('{} {} {}' .format(weekdag,dag,maand))
print('{} {} {} om {}.{} uur'.format(weekdag,dag,maand,uur,minuten))


lst = ['Alan Turing', 'Ken Thompson', 'Vint Cerf']
for name in lst:
    fl = name.split()
    print(fl[0],fl[1])

For