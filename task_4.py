n = int(input("Введите n: "))

f = []
for i in range(n + 1):
    start = i * i + 1
    end = i * i + i + 1
    f_i = sum(1 / j for j in range(start, end + 1))
    f.append(f_i)
    print(f"f_{i} = {f_i:.6f}")

product = 1
for val in f:
    product *= val
print(f"\nПроизведение f_0*f_1*...*f_{n} = {product:.10f}")