# Делаем bubble sort вручную...
def sort_list(l):
    l = list(l)
    for i in range(1, len(l)):
        for j in range(i):
            if l[i] < l[j]:
                (l[i], l[j]) = (l[j], l[i])
    return l

def all_sort(*args):
    # return sorted(args)
    return sort_list(args)

print(all_sort(7, 6, 1, 3, 8, 0, -2))