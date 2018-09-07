def d (n):
     L = [1]
     i=1
     while i<n:
       yield(L)
       c= len(L)-1
       k = [L[j]+L[j+1] for j in range(c)]
       L = [1]+k+[1]
       i=i+1

for t in d(6):
print(t)