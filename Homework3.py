# Task 1
little_bottles = int(input("Введите количество маленьких бутылок: "))
big_bottles = int(input("Введите количество больших бутылок: "))

little_bottles_price = little_bottles * 0.10
big_bottles_price = big_bottles * 0.25
total_price = little_bottles_price + big_bottles_price

print(f"Общая сумма всех бутылок = {total_price}$")


# Task 2
total_order = int(input("Общая сумма вы должны платить = "))
bill = total_order * 0.10
tip = total_order * 0.18
remainder = total_order - (bill + tip)
print(f"Из них:\n"
      f"\tЧаевые для офитсианта = {tip}$\n"
      f"\tНалог = {bill}$\n"
      f"\tСумма вашего заказа = {remainder}$")

# Task 3
number = int(input("Введите число: "))

if number > 0:
    summ = (number * (number + 1)) / 2
    print(f"Сумма натуральных чисел: {summ}")

else:
    print("Введите положительное число.")

# Task 4

suviner = 75
bezdelushka = 112

s = int(input("Введите количество сувинеров: "))
b = int(input("Введите количество безделушек: "))

summa = ((s * suviner) + (b * bezdelushka))

print(f"Общий вес посылок составляет = {summa}гр\n"
      f"Из них:\n"
      f"\tБезделушки = {bezdelushka * b}гр\n"
      f"\tСувинеры = {suviner * s}гр")