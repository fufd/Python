def cc(L):
        for a in L:
            for b in L:
                if a == min(L) and b == max(L):
                    return(a,b)
a=[1,6,3]
b=cc(a)
print(b)