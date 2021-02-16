a = 3
b = 4
d = "ky"
print(a + b)
print(d)
c = input()
print(c)

print("-" * 30)

time = int(input("Введите сек:"))
cek = time % 60
m1 = time // 60
m = cek %60
c = m1 // 60
print(f"{c:02}:{m1:02}:{cek:02}")


print("-" * 30)
n = int(input("число n:"))
k = str(n)
k1 = k + k
k2 = k + k + k
z = n + int(k1) + int(k2)
print(z)

print("-" * 30)
x = int(input(" Введите число:"))
max = 0
while x > 0:
    d = x % 10
    x //= 10
    if d > max:
        max = d
print(max)

print("-" * 30)
a = float(input("Введите выручку"))
b = float(input("Введите издержки"))

if a > b:
    print(f"Прибыль:{a - b}")
    print(f"Рентабельность:{(a - b) / a}")
    c = int(input("Введите кол-во сотрудников:"))
    print(f"Прибыль на одного сотрудника:{(a - b) / c}")
else:
    print(f"Убыток:{b - a}")

print("-" * 30)
a = float(input("Первый км"))
b = float(input("Последний км"))
c = 1
while a < b:
    a *= 1.1
    c += 1
print(f"На {c} дней спортсмен пробежал {b} км ")
