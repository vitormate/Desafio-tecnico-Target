num = int(input('Informe um número para saber se ele pertence a sequência de Fibonacci: '))

x = 0
y = 1
belongs = False


if num == x or num == y:
    belongs = True

while y < num:    
    temp = x
    x = y
    y += temp
    if y == num:
        belongs = True

if belongs:
    print(f'{num} pertence a sequência de Fibonacci')
else:
    print(f'{num} não pertence a sequência de Fibonacci')