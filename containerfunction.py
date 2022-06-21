

x = ( 1, 2, 3, 4, 5 )
h = ( 6, 7, 8, 9, 10)
f = reversed(x)
g = list(reversed(x))
a = sum(x)
b = max(x)
d = any(x)
e = all(x)
z = zip( x, h )
for a, b in z: print(f'{a} - {b}')

x = ('cat', 'dog', 'rabbit', 'raptor')  #enumerate
for i, v in enumerate(x): print(f'{i}: {v}')

