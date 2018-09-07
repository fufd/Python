L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(L)
def byname(T):
    return T[0]

def byscore(t):
    return t[1]

a = sorted(L, key=byname)
b = sorted(L, key=byscore,reverse=True)
print(a)
print(b)