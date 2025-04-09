from random import randint
import matplotlib.pyplot as plt

# Создаем данные
X = list(range(101))
Y = [ randint(1, 200) for _ in range(101) ]  # Рандомные значения

# Создаем график
fig, ax = plt.subplots()
ax.plot(X, Y, color="#99b8ff", linewidth=3)

# Устанавливаем заголовок
ax.set_title("Название графика",
             fontsize=24,
             pad=20,
             color="white"
             )
# Устанавливаем названия осей
ax.set_xlabel("Значения по X координате", fontsize=18, color="white")
ax.set_ylabel("Значения по Y координате", fontsize=18, color="white")

# Устанавливаем фон графика
ax.set_facecolor("#161683")

# Показываем сетку
ax.grid(True, linestyle="--", alpha=0.6)

# Цвет подписей тиков (меток на осях)
ax.tick_params(axis='both', colors='white')

# Устанавливаем метки на осях
plt.xticks(list(range(0, 101, 10)))

# Устанавливаем горизонтальную линию на графике
plt.axhline(y=sum(Y) / 101, color="yellow",
            linestyle="--", label="Среднее значение")

# Добавляем легенду графика
plt.legend(loc="upper left", facecolor="#02102c", labelcolor="white")

# Изменяем размер и цвет вне графика
fig.set_size_inches(20, 8)  # В дюймах
fig.set_facecolor("#02102c")

# Сохраняем график в файл (указывайте путь и формат: .png, .jpg, .pdf)
fig.savefig("charts/beautiful_chart.png",
            dpi=100,  # dpi - разрешение
            bbox_inches="tight"  # Обрезание белых полей вокруг графика
            )
