# VK_group_members_task

Была проведена работа:
1.Создан скрипт выгрузки данных о участниках группы ВК при помощи VK API.Полученные данные были записаны в CSV-файл и сохранены локально.
2.На базе Postgres создана таблица group_members, куда были выгружены данные из сохраненного файла CSV. В поле таблицы lаst_seen изменен формат данных с unix на timestamp для информативности.
3.На основе полученной таблицы были проведены расчеты, указанные в тестовом задании (в файле скриптов прокомментировано).
4.Были созданы диаграммы при помощи визуализационных библиотек python. Содержание прокомментировано в файлах.
5.Все файлы были выгружены в репозиторий на github.
Часть тестового задания, требующего написания скриптов на Pyhton, была написана здесь:
https://colab.research.google.com/drive/1LZJB5HJeGNhC0eAI1HgON5kr2sspKQKv?usp=sharing
(По ссылке так же сохранены черновики разрабатываемых скриптов, которые по той или иной причине не работали. Сохранены для наглядности)
