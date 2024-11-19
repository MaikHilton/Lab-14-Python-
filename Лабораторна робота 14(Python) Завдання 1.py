import numpy as np
import matplotlib.pyplot as plt

# Створення масиву значень x від -2 до 2, за виключенням 0, щоб уникнути ділення на 0
x = np.linspace(-2, 2, 100)
x = x[x != 0]  # виключаємо x=0

# Визначаємо функцію Y(x)
y = np.sin(x) * (1 / x) * np.cos(x**2 + 1 / x)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', linewidth=2, linestyle='-', label=r'$Y(x) = \sin(x) \cdot \left( \frac{1}{x} \right) \cdot \cos\left(x^2 + \frac{1}{x}\right)$')

# Додавання назви графіка, позначення осей та легенду
plt.title('Графік функції $Y(x) = \sin(x) \cdot (1/x) \cdot \cos(x^2 + 1/x)$')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.legend()

# Відображення графіка
plt.grid(True)
plt.show()
