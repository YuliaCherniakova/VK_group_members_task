#задание с диаграммой топ-5 имен
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\Users\user\Desktop\group_members.csv')
# Группировка по имени и подсчет количества участников с каждым именем
top_names = df.groupby('firstname').size().reset_index(name='count')

# Сортировка по убыванию количества участников
top_names = top_names.sort_values('count', ascending=False)
# Выбираем топ 5 имен
top_5_names = top_names.head(5)

# Создание диаграммы
plt.bar(top_5_names['firstname'], top_5_names['count'])
plt.xlabel('Имя')
plt.ylabel('Количество участников')
plt.title('Топ 5 самых популярных имен среди участников группы')
plt.show()


#задание диаграмма рассеяния
#подсчет возраста
df['age'] = 2024 - pd.to_datetime(df['bdate']).dt.year

# Создаем диаграмму рассеяния
plt.scatter(df['age'], df['friends_count'])
plt.xlabel('Возраст')
plt.ylabel('Количество друзей')
plt.title('Рассеяние: Возраст участников и количество друзей')
plt.show()