def notis(n, a, notificaciones):
    subs = a

    for notificaciones in notificaciones:
        if notificaciones == '+':
            subs += 1
        else:
            subs = max(0, subs - 1)

    if subs == n:
        return "YES"
    elif subs >= a:
        return "MAYBE"
    else:
        return "NO"

t = int(input())

for _ in range(t):
    n, a, q = map(int, input().split())
    notificaciones = input()

    result = notis(n, a, notificaciones)
    print(result)
