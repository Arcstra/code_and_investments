from random import randint
import seaborn as sns
import matplotlib.pyplot as plt

# Данные (матрица 12x12)
data = [[randint(-20, 20) for _ in range(12)] for i in range(12)]

# Настройка стиля (опционально)
plt.style.use("dark_background")  # Для темного фона
plt.figure(figsize=(14, 12))  # Размер

# Создаем тепловую карту
heatmap = sns.heatmap(
    data,
    annot=True,              # Показывать значения в ячейках
    annot_kws={"size": 16},  # Размер аннотаций
    xticklabels=False,       # Убрать метки на оси X
    yticklabels=False,       # Убрать метки на оси Y
    cmap="magma",            # Цветовая схема: "coolwarm", "viridis", "YlGnBu"
    vmin=-20, vmax=20,       # Диапазон значений для цветовой шкалы
    cbar=True,               # Показать цветовую шкалу
)

# Настройка заголовка и осей
plt.title("Title", size=24)
plt.xlabel("XLabel", size=18)
plt.ylabel("YLabel", size=18)

# Настройка цветовой шкалы (справа)
cbar = heatmap.collections[0].colorbar
cbar.ax.tick_params(labelsize=14)

# Сохраняем график в файл (указывайте путь и формат: .png, .jpg, .pdf)
plt.savefig("charts\easy_heatmap.png",
            dpi=100,  # dpi - разрешение
            bbox_inches="tight"  # Обрезание белых полей вокруг графика
            )
