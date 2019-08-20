# Lambda calculus in Python 3

# plain rec factorial (named recursion)
fac = lambda n: 1 if n == 0 else fac(n-1) * n
# print(fac(5))

# omega
ω = lambda f: f(f)

# factor-ish (prepare fac for omega)
fact = lambda f: lambda n: 1 if n==0 else f(f)(n-1) * n

# together now
print(ω(fact)(5))

# fibi (prepare fibi for omega)
fibi = lambda f: lambda n: 1 if n==0 else 1 if n==1 else f(f)(n-1) + f(f)(n-2)

# together now
print(ω(fibi)(6))

# no external names recursion
print(
  (lambda h: h(h))
   (lambda f: lambda n: 1 if n==0 else f(f)(n-1) * n)
    (5)
)

# clockwork orange
print(
  (lambda h: h(h))
   (lambda f: lambda n: 1 if n==0 else 1 if n==1 else f(f)(n-1) + f(f)(n-2))
    (6)
)
