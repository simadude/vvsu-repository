def coolfun(lName, lAge):
    d = {}
    if len(lName) != len(lAge):
        print("Списки имеют разную длину")
        print(d)
        return
    for name, age in zip(lName, lAge):
        d[name] = age
    print(d)

coolfun(["Ann", "Tim", "Sam"], [12, 23, 17])

# coolfun(["Ann", "Tim", "Sam"], [12, 23, 17, 45])