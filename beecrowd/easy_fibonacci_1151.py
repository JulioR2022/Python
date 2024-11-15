en = int(input()) # Entrada do programa
count = 2
fibonacci_list = [0, 1] # fibonacci_list[n] = fibonnaci(n)
print('0 1', end='')

while count < en:
    res = fibonacci_list [count - 1] + fibonacci_list [count -2]
    fibonacci_list .append(res)
    print(' ' + str(res), end='')
    count +=1
print()