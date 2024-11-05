def str_lower(s):
    l = s.split(" ")
    l = list(map(lambda w: w.lower(), l))
    return l

print(str_lower("В лесу родилась ёлочка В лесу она росла"))