from math import ceil
t= int(input())
    n = int(input())
    a= [*map(int, input().split())]
    min= abs(a[0])
    for x in a [1:]:
        if abs(x) < min:
            min=abs(x)
    print(min