print([x*x for x in range(1,11) if x ==8]
      )
print([m*n for m in range(1,5) for n in range(6,11)])
L = ['Hello', 'World', 18, 'Apple', None]
l1=[s.lower() for s in L if isinstance(s,str)]
print(type(L))
print(l1)
