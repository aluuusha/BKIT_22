lst = [1, 2, 3]
print([(i, i**2) for i in lst])
print(list(map(lambda x: (x, x**2), lst)))
print(list(zip(lst,map(lambda x: x**2, lst))))