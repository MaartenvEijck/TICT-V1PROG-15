def convert(TC):
    TF = TC * 1.8 + 32
    return TF


def table():
    print('    {0:7}{1:2}'.format("F","C"))
    for i in range(-30, 41, 10):
        tempf = convert(i)
        print('{0:5}{1:7}'.format(tempf,float(i)))

table()