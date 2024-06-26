/*Выдать топ-3 города, в которых среднее кол-во друзей участников группы самое наибольшее.
Для этого использутеся следующий алгоритм:
Участники группируются по городам и затем находится среднее кол-во друзей в группе.
Затем результат сортирутеся от большего к меньшему и ограничивается первыми тремя результатами
*/
SELECT city, AVG(friends_count) AS avg_friends
FROM group_members
GROUP BY city
ORDER BY avg_friends DESC
LIMIT 3;

/*Какой город самый часто встречаемый у участников этой группы
 участники группируются по городам и агрегатной функцией считается кол-во повторений опредленного города у участников
 сортируется по убыванию и ограничивается первым местом
 */
SELECT city, COUNT(city) AS city_count
FROM group_members
GROUP BY city
ORDER BY city_count DESC
LIMIT 1;