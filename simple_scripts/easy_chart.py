from random import randint
import matplotlib.pyplot as plt

# Создаем данные
X = list(range(100))
Y = [ randint(1, 200) for _ in range(100) ]  # Рандомные значения

# Создаем график
plt.plot(X, Y)

# Сохраняем график в файл (указывайте путь и формат: .png, .jpg, .pdf)
plt.savefig("charts/easy_chart.png", dpi=300)  # dpi - разрешение
