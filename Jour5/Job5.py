liste = [0, 1]
def Job5(liste, i):
    n = liste[-1] + liste[-2]
    liste.append(n)
    if len(liste) == i:
        print(liste[-1])
    else:
        Job5(liste, i)

Job5(liste, 15)