import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = sns.load_dataset('penguins')
print(df.head())

#Завдання 1#
sns.countplot(data=df, x='species')
plt.title('Кількість Пінгвінів за Видами')
plt.xlabel('Вид Пінгвіна')
plt.ylabel('Кількість Спостережень')
plt.show()

#Завдання 2#
sns.countplot(data=df, x='species', hue='sex', palette='muted')
plt.title('Кількість Пінгвінів за Видами та Статтю')
plt.xlabel('Вид Пінгвіна')
plt.ylabel('Кількість Спостережень')
plt.legend(title='Стать')
plt.show()

#Завдання 3#
sns.barplot(data=df, x='species', y='body_mass_g', palette='pastel')
plt.title('Середня Маса Тіла за Видами Пінгвінів')
plt.xlabel("Вид Пінгвіна")
plt.ylabel('Середня Маса Тіла (г)')
plt.show()

#Завдання 4#
sns.barplot(data=df, x='species', y='body_mass_g', hue='sex', palette='deep')
plt.title('Середня Маса Тіла за Видами Пінгвінів та Статтю')
plt.xlabel('Вид Пінгвіна')
plt.ylabel('Середня Маса Тіла (г)')
plt.legend(title='Стать')
plt.show()

#Завдання 5#
sns.barplot(data=df, x='species', y='body_mass_g', estimator=np.sum, palette='coolwarm')

plt.title('Сумарна Маса Тіла за Видами Пінгвінів')
plt.xlabel('Вид Пінгвіна')
plt.ylabel('Сумарна Маса Тіла (г)')

plt.show()

#Завдання 6#
sns.barplot(data=df, x='species', y='body_mass_g', hue='sex', estimator=np.median, palette='Set1')

plt.title('Медіанні Маси Тіла за Видами Пінгвінів та Статтю')
plt.xlabel('Вид Пінгвіна')
plt.ylabel('Медіанна Маса Тіла (г)')
plt.legend(title='Стать')

for p in plt.gca().patches:
    plt.annotate(format(p.get_height(), '.1f'),
                 (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center',
                 xytext=(0, 9),
                 textcoords='offset points')

plt.show()

#Завдання 7#
sns.barplot(data=df, x='species', y='body_mass_g', estimator=np.mean, ci='sd', palette='viridis')

plt.title('Середня Маса Тіла за Видами Пінгвінів з Стандартним Відхиленням')
plt.xlabel('Вид Пінгвіна')
plt.ylabel('Середня Маса Тіла (г)')

for p in plt.gca().patches:
    plt.annotate(format(p.get_height(), '.1f'),
                 (p.get_y() + p.get_height() / 2., p.get_height()),
                 ha='center', va='center',
                 xytext=(0, 10),
                 textcoords='offset points')

plt.show()
