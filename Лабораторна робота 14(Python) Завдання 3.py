import json
import matplotlib.pyplot as plt

# Шлях до JSON файлу
FILE_PATH = 'train_schedule.json'

# Функція для завантаження розкладу
def load_schedule():
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {FILE_PATH} не знайдено. Будь ласка, додайте дані про поїзди.")
        return {}

# Функція для підрахунку поїздів у трьох часових діапазонах
def trains_by_time(schedule):
    morning_trains = 0
    day_trains = 0
    evening_trains = 0

    for details in schedule.values():
        arrival_hour = details['arrival'][0]
        
        if arrival_hour < 9:
            morning_trains += 1
        elif 9 <= arrival_hour < 18:
            day_trains += 1
        else:
            evening_trains += 1

    return morning_trains, day_trains, evening_trains

# Функція для побудови кругової діаграми
def plot_pie(morning, day, evening):
    labels = ['До 9:00', 'З 9:00 до 18:00', 'З 18:00 до 24:00']
    sizes = [morning, day, evening]
    colors = ['#ff9999', '#66b3ff', '#99ff99']

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=100)
    plt.title("Розподіл поїздів за часом прибуття")
    plt.axis('equal')
    plt.legend(labels, title="Час прибуття", loc="center right", bbox_to_anchor=(1.1, 0.0))
    plt.show()

# Основний код для виконання завдання
schedule = load_schedule()
morning_trains, day_trains, evening_trains = trains_by_time(schedule)
plot_pie(morning_trains, day_trains, evening_trains)
