import csv
import random
import string


def generate_random_string(length=8):
    letters = string.ascii_lowercase
    return "".join([random.choice(letters) for i in range(length)])


def generate_email():
    domains = ["gmail.com", "yandex.ru", "mail.ru", "outlook.com"]
    username = generate_random_string(8)
    selected_domain = random.choice(domains)
    return f"{username}@{selected_domain}"


def generate_users_data(count=100):
    male_first_names = ["Иван", "Сергей", "Алексей", "Дмитрий", "Пётр"]
    male_last_names = ["Иванов", "Петров","Сидоров","Смирнов","Кузнецов","Попов","Васильев","Соколов","Новиков",]

    female_first_names = ["Анна", "Мария", "Елена", "Ольга", "Наталья"]
    female_last_names = [name + "а" for name in male_last_names]

    with open("users_data.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Имя", "Фамилия", "Email"])

        for i in range(count):
            # Сначала случайно выбираем пол (0 - мужской, 1 - женский)
            gender = random.choice(["male", "female"])

            if gender == "male":
                first_name = random.choice(male_first_names)
                last_name = random.choice(male_last_names)
            else:
                first_name = random.choice(female_first_names)
                last_name = random.choice(female_last_names)

            email = generate_email()
            writer.writerow([first_name, last_name, email])

    print(f"Успешно сгенерировано {count} пользователей в файл 'users_data.csv'!")


generate_users_data(50)
