print("Вычисление суммы")

total_sum = 0

for k in range(1, 11):
    inner_sum = 0
    for l in range(1, 16):
        inner_sum += (k - l) ** 2

    term = k ** 3 * inner_sum
    total_sum += term

    print(f"k = {k}: k^3 = {k ** 3}, ∑^15 (k-l)^2 = {inner_sum}, слагаемое = {term}")

print(f"Результат: S = {total_sum}")

