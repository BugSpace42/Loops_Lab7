n = int(input("Введите количество чисел n: "))
numbers = []

print(f"Введите {n} чисел:")
for i in range(n):
    num = int(input(f"q_{i+1}: "))
    numbers.append(num)

result_a = []
result_b = []
result_c = []

# Удвоенные нечётные числа
for num in numbers:
        if num % 2 == 0 and (num // 2) % 2 != 0:
            result_a.append(num)
print("а) Удвоенные нечетные числа:")
if result_a:
    print(result_a)
else:
    print("Таких чисел нет")