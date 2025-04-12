import matplotlib.pyplot as plt

# Цена акций на 1 апреля 2010 года
data_start_price = [253.55, 2570, 234.35, 86.40, 172.49]
# Компании-эмитенты
issuers = ["МТС", "Магнит", "Роснефть", "Сбер", "Газпром"]
colors = ["white", "red", "yellow", "#19d294", "#2f5ee9"]

# Выплаты дивидендов за каждый год
data_div = {
    2010: [15.4, 6.57, 2.76, 0.92, 3.85],
    2011: [14.5, 22.93, 7.53, 2.08, 8.97],
    2012: [14.7, 81.35, 8.05, 2.57, 5.99],
    2013: [19.8, 135.21, 12.85, 3.2, 7.2],
    2014: [24.8, 362.94, 8.21, 0.45, 7.2],
    2015: [25.2, 310.47, 11.75, 1.97, 7.89],
    2016: [26.0, 278.13, 5.98, 6.00, 8.0397],
    2017: [26.0, 251.01, 10.48, 12.00, 8.04],
    2018: [26.0, 304.16, 25.91, 16.00, 16.61],
    2019: [28.66, 304.19, 33.41, 18.70, 15.24],
    2020: [29.50, 490.62, 6.94, 18.70, 12.55]
}

# Создаем данные
X = list(range(2010, 2021))

fig, ax = plt.subplots()

for i in range(5):
    Y = [0] * 11
    for j in range(2010, 2021):
        Y[j - 2010] = (data_div[j][i] / data_start_price[i]) * 100
    # Создаем график
    ax.plot(X, Y, color=colors[i], label=issuers[i], linewidth=2.5)

# Устанавливаем заголовок
ax.set_title("Дивидендная доходность",
             fontsize=24,
             pad=20,
             color="white"
             )
# Устанавливаем названия осей
ax.set_xlabel("Года, г.", fontsize=18, color="white")
ax.set_ylabel("Дивидендная доходность, %", fontsize=18, color="white")

# Устанавливаем фон графика
ax.set_facecolor("#1f0d3f")

# Показываем сетку
ax.grid(True, linestyle="--", alpha=0.6)

# Цвет подписей тиков (меток на осях)
ax.tick_params(axis='both', colors='white')

# Устанавливаем метки на осях
plt.xticks(list(range(2010, 2021)))
plt.yticks(list(range(0, 25, 2)))

# Добавляем легенду графика
plt.legend(loc="upper left", fontsize=16, facecolor="#02102c", labelcolor="white")

# Изменяем размер и цвет вне графика
fig.set_size_inches(16, 9)  # В дюймах
fig.set_facecolor("#141023")

# Сохраняем график в файл (указывайте путь и формат: .png, .jpg, .pdf)
plt.savefig("charts/dividend_yield_chart.png",
            dpi=200,   # dpi - разрешение
            bbox_inches="tight"  # Обрезание белых полей вокруг графика
            )
