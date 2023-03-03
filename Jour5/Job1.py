def facto(n):
    if n == 0:
        return 1
    else:
        return n * facto(n - 1)


print("Entrer un nombre entier: ")
n = input()
print(facto(int(n)))