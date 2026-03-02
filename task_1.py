def get_divisors_sum(n):
    # Вычисляет сумму собственных делителей числа n.
    if n <= 1:
        return 0

    sum = 1
    for i in range(2, n):  # Не включаем n, т.к. нужно найти сумму не всех делителей, а только собственных
        if n % i == 0:
            sum += i

    return sum

def classify(n, sum):
    # Классифицирует число, исходя из суммы его делителей
    categories = []

    # Совершенные числа: s(n) = n
    if sum == n:
        categories.append("совершенное")

    # Недостаточные числа: s(n) < n
    if sum < n:
        categories.append("недостаточное")

    # Избыточные числа: s(n) > n
    if sum > n:
        categories.append("избыточное")

    # Простые числа: s(n) = 1 (только для n > 1)
    if sum == 1 and n > 1:
        categories.append("простое")

l = int(input("Введите левую границу в диапазоне: "))
r = int(input("Введите правую границу в диапазоне: "))
for i in range(l, r + 1):
    s = get_divisors_sum(i)
    print(f"Сумма собственных делителей числа {i}: {s}")
