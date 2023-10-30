import random
import json
import csv
import os

# Глобальные переменные
save_file = "game_save.json"
player_data_file = "player_data.csv"

# Функция для вывода текста и ожидания ввода игрока
def display_text(text):
    print(text)
    input("Нажмите Enter для продолжения...")

# Функция для представления вариантов выбора и получения ответа от игрока
def get_choice(choices):
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")

    while True:
        try:
            choice = int(input("Выберите вариант (1-{}): ".format(len(choices))))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Пожалуйста, выберите корректный вариант.")
        except ValueError:
            print("Пожалуйста, введите число.")

# Функция для загрузки сохранения из JSON файла
def load_game():
    try:
        with open(save_file, 'r') as save_data:
            data = json.load(save_data)
            return data
    except FileNotFoundError:
        return None

# Функция для сохранения игры в JSON файл
def save_game(location, inventory):
    data = {
        "location": location,
        "inventory": inventory
    }
    with open(save_file, 'w') as save_data:
        json.dump(data, save_data)

# Функция для удаления сохранения
def delete_save():
    try:
        os.remove(save_file)
        print("Сохранение удалено.")
    except FileNotFoundError:
        print("Сохранение не найдено.")

# Функция для записи данных игроков в CSV файл
def write_player_data(player_name, location, inventory):
    with open(player_data_file, mode='a', newline='') as player_data:
        player_writer = csv.writer(player_data)
        player_writer.writerow([player_name, location, ', '.join(inventory)])

# Основная функция игры
def main():
    inventory = []  # Список для инвентаря игрока
    location = "начало"  # Начальное местоположение игрока

    player_name = input("Введите ваше имя: ")

    saved_data = load_game()
    if saved_data:
        location = saved_data["location"]
        inventory = saved_data["inventory"]
        print("Загружено сохранение.")

    while True:
        if location == "начало":
            display_text("Вы находитесь в начале приключения. Вы видите два пути перед собой.")
            choice = get_choice(["Идти налево", "Идти направо"])

            if choice == 1:
                location = "лес"
                display_text("Вы направляетесь в лес.")
            else:
                location = "пещера"
                display_text("Вы направляетесь к пещере.")

        elif location == "лес":
            display_text("Вы находитесь в лесу. Вы видите ручку и меч.")
            choice = get_choice(["Взять ручку", "Взять меч", "Вернуться назад"])

            if choice == 1:
                inventory.append("ручка")
                display_text("Вы взяли ручку и добавили ее в инвентарь.")
            elif choice == 2:
                inventory.append("меч")
                display_text("Вы взяли меч и добавили его в инвентарь.")
            else:
                location = "начало"

        elif location == "пещера":
            display_text("Вы вошли в пещеру и увидели сундук.")
            choice = get_choice(["Открыть сундук", "Вернуться назад"])

            if choice == 1:
                if "меч" in inventory:
                    display_text("Вы открываете сундук и находите сокровища! Поздравляем, вы выиграли!")
                    write_player_data(player_name, location, inventory)
                else:
                    display_text("Сундук заперт, и у вас нет подходящего инструмента для открытия.")
            else:
                location = "начало"

        play_again = input("Хотите ли вы сыграть еще раз? (да/нет): ").lower()
        if play_again != "да":
            break

        save_game(location, inventory)  # Сохраняем игру

if __name__ == "__main__":
    main()
