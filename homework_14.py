import numpy as np
import matplotlib.pyplot as plt

categories1 = ['Продукт A', 'Продукт B', 'Продукт C', 'Продукт D']
values1 = [50, 75, 30, 90]

categories2 = ['A', 'B', 'C', 'D', 'E']
values2 = [10, 20, 15, 30, 25]
colors2 = ['red', 'blue', 'green', 'orange', 'purple']

athletes = ['A', 'B', 'C']
medals = [5, 10, 7]

countries = ['США', 'Канада', 'Мексика', 'Бразилія']
gdp = [21.43, 1.74, 1.22, 2.05]

cities = ['Прага', 'Брно', 'Острава', 'Пльзень']
jan_temp = [-1, 0, -2, 1]
jul_temp = [23, 22, 24, 23]
x = np.arange(len(cities))

plt.style.use("seaborn-v0_8")
fig, axs = plt.subplots(3, 2, figsize=(15, 12))
fig.suptitle("Демонстрація барчартів (Завдання 1–5)", fontsize=20, fontweight="bold")

axs[0, 0].bar(categories1, values1, color="blue", edgecolor="black", alpha=0.7)
axs[0, 0].set_title("Завдання 1: Продажі")
axs[0, 0].set_xlabel("Категорії продуктів")
axs[0, 0].set_ylabel("Обсяг продажів")
axs[0, 0].grid(axis="y", linestyle="--", alpha=0.5)

axs[0, 1].bar(categories2, values2, color=colors2, edgecolor="black", linewidth=1.5)
axs[0, 1].set_title("Завдання 2: Різнокольорові стовпці")
axs[0, 1].set_xlabel("Категорії")
axs[0, 1].set_ylabel("Значення")

bars = axs[1, 0].bar(athletes, medals, color="gold", edgecolor="black")
axs[1, 0].set_title("Завдання 3: Медалі спортсменів")
axs[1, 0].set_xlabel("Спортсмени")
axs[1, 0].set_ylabel("Кількість медалей")
axs[1, 0].bar_label(bars, fmt="%d", padding=3)

axs[1, 1].barh(countries, gdp, color="lightblue", edgecolor="black", alpha=0.8)
axs[1, 1].set_title("Завдання 4: ВВП країн")
axs[1, 1].set_xlabel("ВВП (трильйони доларів)")
axs[1, 1].set_ylabel("Країни")

axs[2, 0].bar(x - 0.2, jan_temp, width=0.4, label="Січень", color="blue")
axs[2, 0].bar(x + 0.2, jul_temp, width=0.4, label="Липень", color="orange")
axs[2, 0].set_xticks(x)
axs[2, 0].set_xticklabels(cities, rotation=30, ha="right")
axs[2, 0].set_title("Завдання 5: Порівняння температур")
axs[2, 0].set_xlabel("Міста")
axs[2, 0].set_ylabel("Температура (°C)")
axs[2, 0].legend()

axs[2, 1].axis("off")
axs[2, 1].text(0.5, 0.5, "🎉 Барчарт-party 🎉", ha="center", va="center", fontsize=16, fontweight="bold")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

np.random.seed(42)
categories = [f"Cat{i}" for i in range(1, 21)]
groups = 5
x = np.arange(len(categories))

plt.style.use("ggplot")
fig, ax = plt.subplots(figsize=(20, 10))

colors = ['blue', 'green', 'red', 'orange', 'purple']
width = 0.15

for i in range(groups):
    vals = np.random.randint(5, 100, size=len(categories))
    ax.bar(
        x + (i - groups/2)*width, 
        vals, 
        width=width, 
        color=colors[i % len(colors)], 
        edgecolor='black', 
        linewidth=1.5, 
        alpha=0.7, 
        label=f"Група {i+1}"
    )

ax.set_title("МЕГА-БАРЧАРТ з усіма можливими налаштуваннями", fontsize=18, fontweight='bold')
ax.set_xlabel("Категорії", fontsize=14)
ax.set_ylabel("Значення", fontsize=14)
ax.grid(axis='y', linestyle='--', alpha=0.6)
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha="right")
ax.legend(ncol=groups, loc="upper center", bbox_to_anchor=(0.5, 1.1))

for container in ax.containers:
    ax.bar_label(container, fmt='%d', padding=2, fontsize=8, rotation=90)

plt.tight_layout()
plt.show()

pie_data = [
    ([30, 30, 20, 20], ['A', 'B', 'C', 'D'], "Проста діаграма"),
    ([40, 35, 15, 10], ['Оренда', 'Зарплати', 'Маркетинг', 'Інше'], "Розподіл витрат"),
    ([60, 25, 10, 5], ['A', 'B', 'C', 'D'], "Зсув сегментів", [0.1, 0, 0.5, 0]),
    ([50, 30, 15, 5], ['Категорія 1', 'Категорія 2', 'Категорія 3', 'Категорія 4'], "Розподіл категорій"),
    ([30, 45, 15, 10], ['Тип A', 'Тип B', 'Тип C', 'Тип D'], "Транспортні засоби"),
    ([25, 35, 20, 20], ['A', 'B', 'C', 'D'], "Кільцева діаграма"),
    ([60, 20, 15, 5], ['A', 'B', 'C', 'D'], "Розподіл сегментів"),
]

fig, axs = plt.subplots(3, 3, figsize=(15, 12))
fig.suptitle("Pie charts", fontsize=20, fontweight="bold")

for i, data in enumerate(pie_data):
    row, col = divmod(i, 3)
    sizes, labels, title = data[0], data[1], data[2]
    explode = data[3] if len(data) == 4 else None
    
    axs[row, col].pie(
        sizes, 
        labels=labels, 
        autopct='%1.1f%%', 
        explode=explode if explode else None
    )
    axs[row, col].set_title(title)

axs[2, 2].axis("off")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
