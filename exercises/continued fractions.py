# Lagrange Reduction coincides with euclid's gcd algorithm if the input given is two parallel vectors.
# In particular, it can be used to compute the continued fraction expansion of a given number.

a = 12
b = 25

def LagrangeRed(a, b):
    condition = True
    lista = []
    while condition:
        a,b = b,a
        k = int(round(b/a))
        lista.append(k)
        b -= k*a
        condition = abs(a) > abs(b) and b!= 0
    return lista

lista = LagrangeRed(a,b) # gives continued fraction expansion of a/b
print(lista)

# reconstruct a/b from continued fraction expansion
term = 1/lista[-1]
last = lista[0]
lista.pop(0)
lista.pop()
for i in lista[::-1]:
    term = 1/(i + term)

# sanity check
print(last + term - a/b)