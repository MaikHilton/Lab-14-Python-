import csv
import matplotlib.pyplot as plt

# Ініціалізація списків для України та Німеччини
years = []
ukraine_values = []
germany_values = []

# Читання даних із CSV-файлу
with open('Children out of school (% of primary school age).csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        year = int(row['Year'])
        
        # Перевірка на наявність даних і якщо вони є ,перетворюємо на число 
        ukraine_value = row['Ukraine']
        germany_value = row['Germany']
        
        # Додавання даних у відповідні списки
        years.append(year)
        ukraine_values.append(float(ukraine_value) if ukraine_value else None)
        germany_values.append(float(germany_value) if germany_value else None)

# 2.1 Лінійний графік
plt.figure(figsize=(10, 6))
plt.plot(years, ukraine_values, label='Ukraine', color='blue', marker='o')
plt.plot(years, germany_values, label='Germany', color='orange', marker='o')
plt.xlabel('Year')
plt.ylabel('Children out of school (% of primary school age)')
plt.title('Children out of school (% of primary school age) for Ukraine and Germany')
plt.legend()
plt.grid(True)
plt.show()

# Цикл для вибору країни кілька разів
while True:
    print("Choose a country for bar chart:")
    print("1 - Ukraine")
    print("2 - Germany")
    print("0 - Exit")

    # Отримання вибору від користувача
    choice = int(input("Enter your choice (1, 2, or 0): "))

    if choice == 1:
        selected_values = ukraine_values
        country = 'Ukraine'
    elif choice == 2:
        selected_values = germany_values
        country = 'Germany'
    elif choice == 0:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
        continue  # Повернення до початку циклу

    # Фільтрація для видалення None значень (якщо вони є)
    filtered_years = [year for year, value in zip(years, selected_values) if value is not None]
    filtered_values = [value for value in selected_values if value is not None]

    # Побудова стовпчастої діаграми для обраної країни
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_years, filtered_values, color='purple')
    plt.xlabel('Year')
    plt.ylabel('Children out of school (% of primary school age)')
    plt.title(f'Children out of school (% of primary school age) in {country}')
    plt.grid(axis='y', linestyle='--', linewidth=0.7)
    plt.show()

