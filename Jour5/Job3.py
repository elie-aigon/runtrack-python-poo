i = 0
def job3(string, i):
    if string == "":
        print(i)
    else:
        i += 1
        job3(string[:-1], i)


job3("bonjour", i)