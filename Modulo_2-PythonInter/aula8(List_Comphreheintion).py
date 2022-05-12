""""

"""

l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]

ex3 = [(v,v2) for v in l1 for v2 in range(3)]

print(ex3)

l2 = ['Vinícius', 'Alexander']
ex4 = [v.replace('a', '@') for v in l2]

print(ex4)

ex5 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l1]
print(ex5)