# ! 1.Numeric Data Types -> int, float, complex
a1 = 5
a2 = -10
a3 = 0x34
a4 = 0o34
a5 = 0b1101
# print("The type of a1 is:", type(a1))
# print("The type of a2 is:", type(a2))
# print("The type of a3 is:", type(a3))
# print("The type of a4 is:", type(a4))
# print("The type of a5 is:", type(a5))


b1 = 3.14
b2 = -3.14
b3 = 2e2  # 2*10^2
b4 = 10.
b5 = -3e7
# print("The type of b1 is:", type(b1))
# print("The type of b2 is:", type(b2))
# print("The type of b3 is:", type(b3))
# print("The type of b4 is:", type(b4))
# print("The type of b5 is:", type(b5))

c1 = 3 + 4j
c2 = -3 - 4j
c3 = 4e-10j  # 0+4*10^-10j
c4 = 4.j  # 0+4j
# print("The type of c1 is:", type(c1))
# print("The type of c2 is:", type(c2))
# print("The type of c3 is:", type(c3))
# print("The type of c4 is:", type(c4))

# ! String Data Type -> str
d1 = 'Hello World'
d2 = "It is a sunny day"
d3 = '''this
is a multiline
example'''
d4 = """sentence
multi
line"""
d5 = 'It\'s a sunny day'
# print("The type of d1 is:", type(d1))
# print("The type of d2 is:", type(d2))
# print("The type of d3 is:", type(d3))
# print("The type of d4 is:", type(d4))
# print("The type of d5 is:", type(d5))

# ! Sequence Data Types -> list, tuple, range
e1 = [1, 2, 3, 4, 5]
e2 = ['a', "b", '''c''']
e3 = [1, 2, 3, 'f', '''triple''']
# print("The type of e1 is:", type(e1))
# print("The type of e2 is:", type(e2))
# print("The type of e3 is:", type(e3))


f1 = (1, 2, 3, 4, 5)
f2 = ('a', "b", '''c''')
f3 = (1, 2, 3, 'f', '''triple''')
f4 = (1, 's', (1, 2, 's'), [1, 2, 'f', 'd'])

# print("The type of f1 is:", type(f1))
# print("The type of f2 is:", type(f2))
# print("The type of f3 is:", type(f3))
# print("The type of f4 is:", type(f4))

g1 = range(1, 5)
g2 = range(-1, -10)
# print("The type of g1 is:", type(g1))
# print("The type of g2 is:", type(g2))

# ! Mapping Data Type -> dict (dictionary)
h1 = {'key': 'value'}
h2 = {'Rahul': 25, 'Priya': 30, 'Amit': 22}
h3 = {'key1': 100, 'key2': [1, 2, 3], 'key3': {'key3.1': 'key3.2'}}
# print("The type of h1 is:", type(h1))
# print("The type of h2 is:", type(h2))
# print("The type of h3 is:", type(h3))


# ! Boolean Data Type -> bool
i1 = True
i2 = False
i3 = 5 + True  # (1)
i4 = 5 * False  # (0)
i5 = 10 / (True * 3)  # (0)
# print("The type of i1 is:", type(i1))
# print("The type of i2 is:", type(i2))
# print(i3)
# print(i4)
# print(i5)
#
# if i1:
#     print('will not be printed')
# else:
#     print('will be printed')
#
# print(5<2)


j1 = 0
j2 = 0.0
j3 = 0.0j
j4 = None
j5 = []
j6 = ()
j7 = {}
# print(bool(j1))
# print(bool(j2))
# print(bool(j3))
# print(bool(j4))
# print(bool(j5))
# print(bool(j6))
# print(bool(j7))


k1 = 4
k2 = 4.4
k3 = [1, 2]
# print(bool(k1))
# print(bool(k2))
# print(bool(k3))


# ! Set Data Type -> set, frozenset
l1 = {1, 2, 3}
l2 = {1, 2, 3, 3, 2}
l3 = {1, 2, 3, 'apple', 'banana', 'apple'}
# print("The type of l1 is:", type(l1))
# print("The type of l3 is:", type(l3))
# print(l2)
# print(l3)
#
l4 = frozenset({1, 2, 3, 3})
# print("The type of l4 is:", type(l4))

# ! Binary Data Type -> bytes, bytarray, memoryview

m1 = b'Python'
m2 = 'Python'.encode('utf-8')
m3 = bytes([80, 121, 116, 104, 111, 110])  # 80=P, 121 = y, 116 = t ... 110 = n
m4 = bytes([65, 66, 67, 80])
# print(m1)
# print(m2)
# print(m3)
# print(m4)
# print("The type of m1 is", type(m1))
# print("The type of m2 is", type(m2))
# print("The type of m3 is", type(m3))


n1 = bytearray(2)
n2 = bytearray([1, 2, 3, 4, 5])
n3 = bytearray("Python", "utf-8")
# print(n1)
# print(n2)
# print(n3)
# print("The type of n1 is", type(n1))
# print("The type of n2 is", type(n2))
# print("The type of n3 is", type(n3))


o1 = b'hello'
o2 = bytearray("hello", "utf-8")
mv1 = memoryview(o1)
mv2 = memoryview(o2)
# print(mv1)
# print(mv2)
# print("The type of mv1 is", type(mv1))
# print("The type of mv2 is", type(mv2))


# ! None Data Type -> None

p1 = None
p2 = None
# print("The type of p1 is", type(p1))
# print(None == [])
#
# print(id(p1))
# print(id(p2))