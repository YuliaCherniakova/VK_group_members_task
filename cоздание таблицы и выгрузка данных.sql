-- создание таблицы в базе данных с подходящими типами данных для полей
CREATE TABLE group_members ( 
    id INT PRIMARY key not NULL,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    bdate timestamp,
    contacts TEXT,
    city VARCHAR(255),
    last_seen float,
    friends_count INT
);
-- выгрузка данных из файла CSV
copy group_members(id,firstname,lastname,bdate,contacts,city,last_seen,friends_count)
from 'C:\Users\user\Desktop\group_members.csv'
delimiter ','
csv header;

/*поле last_seen было выгружено в формате float, при этом содержащее unix-дату. 
Я решила переконвертировать поле в int и затем в timestamp для большей наглядности.
*/
ALTER TABLE group_members
ALTER COLUMN last_seen TYPE BIGINT; -- int
 
ALTER TABLE group_members
ALTER COLUMN last_seen TYPE timestamptz --timestamp с часовым поясом
USING to_timestamp(last_seen) AT TIME ZONE 'UTC';

select * from group_members