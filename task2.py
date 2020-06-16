a = int(input("Введите ширину прямоугольника:\n"))
b = int(input("Введите длину прямоугольника:\n"))


def squareCount(x,y):
    if x != 0 and y != 0:
        if y > x:
            n = y//x
            print("количество квадратов с ребром "+str(x)+" равно "+str(n))
            squareCount(x,y%x)
        else:
            n = x // y
            print("количество квадратов с ребром " + str(y) + " равно " + str(n))
            squareCount(x%y, y)

squareCount(a,b)