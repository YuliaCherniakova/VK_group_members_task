#данный скрипт разрабатывался в Google Colaboratory
#https://colab.research.google.com/drive/1LZJB5HJeGNhC0eAI1HgON5kr2sspKQKv?usp=sharing

#инсталляция VK API
#pip install vk_api


#импорт библиотек
from posixpath import sep
import vk_api
import csv
import pandas as pd
import datetime

token = 'a157c913a157c913a157c91357a24f86c4aa157a157c913c71228227ede483611f11300'
# Авторизация в API Вконтакте с использованием токена доступа
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

group_id = 'vk_fishing'

# Получение информации о участниках группы
members = vk.groups.getMembers(group_id=group_id, fields='id,firstname,lastname,bdate,contacts,city,last_seen,friends_count')

# Создание файла CSV
with open('group_members.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'firstname', 'lastname','bdate','contacts', 'city', 'last_seen', 'friends_count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for member in members['items']:
        user_id = member['id']
        firstname = member.get('first_name', '')
        lastname = member.get('last_name', '')
        bdate = member.get('bdate', 'N/A')
        if len(bdate) >= 8:  # Проверка даты рождения на полноту (для расчета возраста нужно учесть год рождения, иначе - N/A)
            age = 2024 - int(bdate[-4:])
        else:
            age = 'N/A'
        contacts = '' # сборка контактов - мобильный телефон или домашний или имейл
        if 'contacts' in member:
            if 'mobile_phone' in member['contacts']:
                contacts += 'Телефон: ' + member['contacts']['mobile_phone'] + '\n'
            if 'home_phone' in member['contacts']:
                contacts += 'Домашний телефон: ' + member['contacts']['home_phone'] + '\n'
            if 'email' in member['contacts']:
                contacts += 'Email: ' + member['contacts']['email'] + '\n'
        city = member.get('city', {}).get('title', 'N/A')
        last_seen = member.get('last_seen', {}).get('time', 'N/A')
        friends_count = member.get('friends_count', '')

        writer.writerow({'id': user_id, 'firstname': firstname, 'lastname': lastname, 'contacts': contacts, 'city': city, 'last_seen': last_seen, 'friends_count': friends_count})

df = pd.read_csv('group_members.csv')
df.to_csv(r'C:\Users\user\Desktop\group_members.csv', sep=',', index=False) #сохранение CSV-файла на локальный диск
