 # Project

all_products = {"Весь склад": {}}
cart = {}

while True:
    admin = input("Что вы хотите сделать? (добавить/продукты/корзина/замена/удаление/выход): ")

    if admin == "добавить":
        product_name = input("Введите название продукта: ")
        product_count = input("Введите количество продукта: ")
        all_products["Весь склад"][product_name] = int(product_count)
        print(f"Продукт {product_name} добавлен")

        if product_name in cart:
            cart[product_name] += int(product_count)
        else:
            cart[product_name] = int(product_count)
        print(f"Продукт {product_name} добавлен в корзину")

    elif admin == "продукты":
        print("Список продуктов и их количество")
        for product, count in all_products["Весь склад"].items():
            print(f"{product}: {count}")

    elif admin == "корзина":
        print("Содержимое корзины:")
        for product, count in cart.items():
            print(f"{product}: {count}")

    elif admin == "замена":
        product_name = input("Введите название продукта, который нужно заменить: ")
        new_product_name = input("Введите название нового продукта: ")
        new_product_count = input("Введите количество нового продукта: ")
        cart[new_product_name] = cart.pop(product_name)
        print(f"Продукт {product_name} заменен на {new_product_name}")

    elif admin == "удаление":
        product_name = input("Введите название продукта, который нужно удалить из корзины: ")
        cart.pop(product_name)
        print(f"Продукт {product_name} удален из корзины")

    else:
        break




# 1
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 22]
chetnie = [i for i in lst if i % 2 == 0]
print(chetnie)

# 2
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 22]
nechetnie = [i for i in lst if i % 2 != 0]
print(nechetnie)

# 3
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 22]
multiple_lst = [i * 2 for i in lst]
print(multiple_lst)

# 4
lst = [i for i in range(1, 21)]
print(lst)

# 5
lst = ["python", "java", "javascript", "php"]
a = [i.upper() for i in lst]
print(a)

# 6
lst = ["python", "java", "javascript", "php"]
word_length = [len(i) for i in lst]
print(word_length)

# 7
lst = [i for i in range(1, 20, 3)]
print(lst)