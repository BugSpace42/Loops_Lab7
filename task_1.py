def get_divisors_sum(n):
    # Вычисляет сумму собственных делителей числа n.
    if n <= 1:
        return 0

    sum = 1
    for i in range(2, n):  # Не включаем n, т.к. нужно найти сумму не всех делителей, а только собственных
        if n % i == 0:
            sum += i

    return sum

n = int(input("Введите n: "))
print(get_divisors_sum(n))