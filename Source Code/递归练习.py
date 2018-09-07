def move(n,a,b,c):
    if n == 1:
        print(a,"上的盘子移动至",c)
    elif n == 2:
        print(a,"上的盘子移动至",b)
        print(a,"上的盘子移动至",c)
        print(b,"上的盘子移动至",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(5,"a","b","c")