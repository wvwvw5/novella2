import random

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

# Функция для генерации случайного числа в заданном диапазоне
def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

# Функция для добавления предмета в инвентарь
def add_to_inventory(item, inventory):
    inventory.append(item)
    display_text(f"Вы взяли {item} и добавили его в инвентарь.")

# Основная функция игры
def main():
    inventory = []  # Список для инвентаря игрока
    location = "начало"  # Начальное местоположение игрока

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
                add_to_inventory("ручка", inventory)
            elif choice == 2:
                add_to_inventory("меч", inventory)
            else:
                location = "начало"
        
        elif location == "пещера":
            display_text("Вы вошли в пещеру и увидели сундук.")
            choice = get_choice(["Открыть сундук", "Вернуться назад"])
            
            if choice == 1:
                if "меч" in inventory:
                    display_text("Вы открываете сундук и находите сокровища! Поздравляем, вы выиграли!")
                else:
                    display_text("Сундук заперт, и у вас нет подходящего инструмента для открытия.")
            else:
                location = "начало"
        
        play_again = input("Хотите ли вы сыграть еще раз? (да/нет): ").lower()
        if play_again != "да":
            break

if __name__ == "__main__":
    main()
