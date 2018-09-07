def c(n):
    s=str(n)
    return s==s[::-1]

L=[56,565,5557,464]

a=list(filter(c,L))
print(a)