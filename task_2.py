n = int(input("Введите количество чисел n: "))
numbers = []

print(f"Введите {n} чисел:")
for i in range(n):
    num = int(input(f"q_{i+1}: "))
    numbers.append(num)