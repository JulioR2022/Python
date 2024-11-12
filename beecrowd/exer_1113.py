x = 0
y = 1

while x != y:
    x,y = map(int,(input().split()))
    res = x - y
    if res < 0:
        print('Crescente')
    elif res > 0:
        print('Decrescente')