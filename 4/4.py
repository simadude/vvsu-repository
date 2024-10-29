grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
 'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
 'Ursula': 4, 'Viktor': 5}

for k, v in grades.items():
    print(k, v)

excel = []
good = []
satisf = []
bad = []
for k, v in grades.items():
    if v == 5:
        excel.append(k)
    elif v == 4:
        good.append(k)
    elif v == 3:
        satisf.append(k)
    elif v == 2:
        bad.append(k)