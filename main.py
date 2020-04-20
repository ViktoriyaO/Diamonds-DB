import cx_Oracle

username = 'viktoriya'
password = 'viktoriya'
databaseName = 'localhost:1521/xe'
connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

print('Запит 1. Вивести категорії та загальну кількість діамантів, які входять до них. \n')
query1 = '''
SELECT cut, COUNT(diamond_index) AS count
    FROM Diamond
GROUP BY cut
ORDER BY count DESC;
'''

cursor.execute(query1)
for row in cursor:
    print(row)


print('\nЗапит 2. Вивести колір та % діамантів з таким кольором серед діамантів усіх кольорів. \n')
query2 = '''
SELECT 
    color, 
    ROUND(COUNT(diamond_index)*100/t.count, 2) AS persent
    FROM Diamond,
    (SELECT COUNT(diamond_index) AS count
    FROM Diamond)t   
GROUP BY  color,
        t.count;
'''

cursor.execute(query2)
for row in cursor:
    print(row)


print('\nЗапит 3. Динаміка залежності прозорості діаманту від кількості діамантів, які мають таку прозорість. \n')
query3 = '''
SELECT Clarity.clarity,
    COUNT(Diamond.diamond_index) AS count
    FROM Diamond 
    INNER JOIN Clarity ON Diamond.clarity = Clarity.clarity
GROUP BY Clarity.clarity
ORDER BY count DESC;
'''

cursor.execute(query3)
for row in cursor:
    print(row)

cursor.close()
connection.close()

