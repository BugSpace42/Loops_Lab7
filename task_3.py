numbers = []

print("Введите 10 действительных чисел:")
for i in range(1, 11):
    num = float(input(f"a_{i}: "))
    numbers.append(num)

total = 0
for i in range(10):
    power = i + 1
    term = numbers[i] ** power
    total += term
    print(f"{numbers[i]}^{power} = {term}")

print(f"Результат вычисления: {total}")