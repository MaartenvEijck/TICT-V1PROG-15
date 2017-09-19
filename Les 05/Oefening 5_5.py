#A
infile = open('voorbeeld 5_5.txt', 'r')
inhoud = infile.read()
print(inhoud)
infile.close()

#B
infile = open ('voorbeeld 5_5.txt', 'r')
inhoud = infile.read()
infile.close()
gesplitst = inhoud.split()
print(gesplitst)

#C
infile = open('voorbeeld 5_5.txt','r')
inhoud = infile.readlines()
infile.close()
print(inhoud)