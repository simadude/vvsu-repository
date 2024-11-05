import math

# def my_log(l):
#     return list(map(lambda x: math.log(x) if x > 0 else None, l))

def my_log(l):
    llog = []
    for x in l:
        if x > 0:
            llog.append(math.log(x))
        else:
            llog.append(None)
    return llog

print(my_log([1, 3, 2.5, -1, 9, 0, 2.71]))