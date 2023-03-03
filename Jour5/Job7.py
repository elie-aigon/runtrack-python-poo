import re
chaine1 = input("Entrez chaîne 1 : ")
chaine2 = input("Entrez chaîne 2 : ")

if chaine1 == chaine2:
    print("1")
else:

    if '*' in chaine2:
        chaine2_reg = chaine2.replace('*', '[a-z]*')
        if re.match(chaine2_reg, chaine1):
            print("1")
        else:
            print("0")
    else:
        print("0")
