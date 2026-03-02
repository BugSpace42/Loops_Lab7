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
    return categories

def analyze(start, end):
    if start < 1:
        print("Ошибка: начальное число должно быть натуральным")
        return
    print(f"Анализ чисел от {start} до {end}")

    numbers_data = {}
    # Вычисляем s(n) для всех чисел в диапазоне
    for n in range(start, end + 1):
        sum = get_divisors_sum(n)
        numbers_data[n] = {
            'sum': sum,
            'categories': classify(n, sum)
        }

    perfect = []
    deficient = []
    abundant = []
    primes = []

    for n in range(start, end + 1):
        if "совершенное" in numbers_data[n]['categories']:
            perfect.append(n)
        if "недостаточное" in numbers_data[n]['categories']:
            deficient.append(n)
        if "избыточное" in numbers_data[n]['categories']:
            abundant.append(n)
        if "простое" in numbers_data[n]['categories']:
            primes.append(n)

    print("Числа по категориям:")
    print("Совершенные числа:", perfect)
    print("Недостаточные числа:", deficient)
    print("Избыточные числа:", abundant)
    print("Простые числа:", primes)

l = int(input("Введите левую границу в диапазоне: "))
r = int(input("Введите правую границу в диапазоне: "))
for i in range(l, r + 1):
    s = get_divisors_sum(i)
    print(f"Сумма собственных делителей числа {i}: {s}")
analyze(l, r)
