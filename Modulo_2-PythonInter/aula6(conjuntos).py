# Sets ou conjuntos não aceitam elementos duplicados
s1 = {1,2,3,4,5,6,7,8,9}
print(s1, type(s1))

# add (adicona elementos), update (atualiza os elementos)
s2 = set()
s2.add(9)
s2.update([10,11,12,13,14,15], [15,6,7,8])
print(s2)

# | (União entre dois elementos)
s3 = s1 | s2
print(s3)

# & intersecção entre dois elementos
s4 = s1 & s2
print(s4)

# - diferença entre os dois elementos
s5 = s1 - s2
print(s5)

# ^ Elemetos que estão nos dois sets, mas não em ambos
s6 = s1 ^ s2
print(s6)