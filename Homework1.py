import random

choices = ["камень", "ножницы", "бумага"]

human_choice = int(input("Введите ваш знак \n"
                         "Камень = 1\n"
                         "Ножницы = 2\n"
                         "Бумага = 3\n"
                         ": "))
computer_choice = random.choice(choices)
print(f"Выбор компютера = {computer_choice}")
if human_choice == 1:
    if computer_choice == "камень":
        print("Ничья!")
    elif computer_choice == "ножницы":
        print("Вы победили!")
    else:
        print("Вы проиграли!")
elif human_choice == 2:
    if computer_choice == "камень":
        print("Вы проиграли!")
    elif computer_choice == "ножницы":
        print("Ничья!")
    else:
        print("Вы победили!")
elif human_choice == 3:
    if computer_choice == "камень":
        print("Вы победили!")
    elif computer_choice == "ножницы":
        print("Вы проиграли!")
    else:
        print("Ничья!")
else:
    print("Неправильный знак!")