contacts = ["Anna", "Alexandra", "Kolya", "Muhammad", "Thomas", "Brayn"]
print(contacts)

user_choice = int(input("1 - для удаления, 2 - для изменения, 3 - для добавления: "))

if user_choice == 1:
    remove_contact = input("Введите контакт для удаления: ")
    contacts.remove(remove_contact)
    print("Ваш контакт был удален из списка!")
    print(contacts)

elif user_choice == 2:
    change_contact = input("Введите контакт для изменения: ")
    position = contacts.index(change_contact)
    new_contact = input("Введите новый контакт: ")
    contacts[position] = new_contact
    print("Контакт успешно изменен!")
    print(contacts)

else:
    add_contact = input("Введите новый контакт: ")
    contacts.append(add_contact)
    print("Новый контакт был добавлен в список!")
    print(contacts)