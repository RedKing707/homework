# Task 1
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

func_sum = lambda a, b: a + b

func_compute = lambda a, b: a - b

func_multiply = lambda a, b: a * b

func_divide = lambda a, b: a / b

while True:
    choise = input("Что хотите сделать? (+, -, *, /, выход):  ")
    if choise == "+":
        print(func_sum(number1, number2))
    elif choise == "-":
        print(func_compute(number1, number2))
    elif choise == "*":
        print(func_multiply(number1, number2))
    elif choise == "/":
        print(func_divide(number1, number2))
    else:
        break


# School Management System
students = {}


def add_student():
    student_name = input("Введите имя студента: ")
    student_level = input("Введите класс студента: ")
    students[student_name] = student_level
    print(f"Студент {student_name} добавлен в {student_level} класс")


def show_students():
    print("Список студентов и их классы:")
    for s, l in students.items():
        print(f"{s}: {l}")


def delete_student():
    show_students()
    remove_student = input("Кого хотите удалить? ")
    if remove_student in students:
        students.pop(remove_student)
        print("Студент был удален из списка!")
    else:
        print("Студент не найден!")


while True:
    admin = input("Что вы хотите сделать? (добавить/удалить/список/выход) ")

    if admin == "добавить":
        add_student()
    elif admin == "список":
        show_students()
    elif admin == "удалить":
        delete_student()
    elif admin == "выход":
        break
    else:
        print("Некорректный ввод. Пожалуйста, попробуйте снова.")