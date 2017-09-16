def new_password(oldpassword,newpassword):
    if oldpassword != newpassword and len(newpassword) >=6:
        for teken in newpassword:
            if teken in '0123456789':
                return True
        return False
    else:
        return False
oud = input('Geef je oude wachtwoord: ')
nieuw = input('Geef je nieuwe wachtwoord: ')
print(new_password(oud, nieuw))

#Correcte wachtwoord --> True
res = new_password('vakProg17', 'python17')
print(res)
#Hetzelfde wachtwoord --> False
print(new_password('huProg17', 'huProg17'))

# Te kort nieuw wachtwoord -->
print(new_password('vakProg17', 'Pro17'))