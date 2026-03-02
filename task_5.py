a = []
for i in range(24):
    a.append(float(input(f"a_{i + 1}: ")))

b = []
for k in range(1, 11):
    b_k = sum(x ** k for x in a)
    b.append(b_k)
    print(f"b_{k} = {b_k:.6f}")

print("Итоговая последовательность:")
print(b)