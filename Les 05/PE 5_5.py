zin = input('Geef een willekeurige zin op: ')

def gemiddelde(zin):
   woorden = zin.split()
   lst = []
   for woord in woorden:
       lst.append(len(woord))
   return sum(lst) / len(lst)



print(gemiddelde(zin))

