def move(n,a,b,c):
    if n == 1:
        print(a,"�ϵ������ƶ���",c)
    elif n == 2:
        print(a,"�ϵ������ƶ���",b)
        print(a,"�ϵ������ƶ���",c)
        print(b,"�ϵ������ƶ���",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(5,"a","b","c")