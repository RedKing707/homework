# Task N1

string = input("Введите слово: ")

if string == string[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")

# Task 2

number = int(input("Введите число: "))
print("Таблица умножения для", number)
for i in range(1, 11):
    print(number, "x", i, "=", number * i)


