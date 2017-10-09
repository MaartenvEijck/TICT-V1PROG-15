cijfers = {'Karel':8, 'Kees':9, 'Pietje':10, 'Hans':6, 'Maikel':8, 'Sander':2, 'Gerrit':10, 'Maarten':7}
for student in cijfers:
    if cijfers[student]>= 9:
        print('{} heeft een {}'.format(student,cijfers[student]))