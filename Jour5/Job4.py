def Job4(liste):
    if len(liste) == 1:
        return liste[0]
    max = Job4(liste[1:])
    return liste[0] if liste[0] > max else max

print(Job4([8, 5, 6, 3, 7, 9, 15, 1]))