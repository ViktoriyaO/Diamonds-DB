import cx_Oracle
import chart_studio
import re
chart_studio.tools.set_credentials_file(username='ViktoriaO', api_key='h0uGcQQ1oqxw2mI8h88b')
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dash

def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[0-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

username = 'viktoriya'
password = 'viktoriya'
database = 'localhost:1521/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()



print('1.Вивести категорії та загальну кількість діамантів, які входять до них. \n')
names=[]
values=[]
query1 = '''
SELECT cut, COUNT(diamond_index) AS count
    FROM Diamond
GROUP BY cut
ORDER BY count DESC
'''

cursor.execute(query1)

for row in cursor.fetchall():
    names.append (row[0])
    values.append(row[1])
bar = go.Bar (x = names, y = values)
bar = py.plot([bar],auto_open = True, file_name = "Plot1")




print("\n2.Вивести колір та % діамантів з таким кольором серед діамантів усіх кольорів.\n")
names=[]
values=[]
query2 = '''
SELECT 
    color, 
    ROUND(COUNT(diamond_index)*100/t.count, 2) AS persent
    FROM Diamond,
    (SELECT COUNT(diamond_index) AS count
    FROM Diamond)t   
GROUP BY  color,
        t.count
'''
cursor.execute(query2)
for row in cursor.fetchall():
    names.append (row[0])
    values.append(row[1])
pie = go.Pie (labels = names, values = values)
pie = py.plot([pie],auto_open = True, file_name = "Plot2",)




print("\n3.Динаміка залежності прозорості діаманту від кількості діамантів, які мають таку прозорість.\n")
names=[]
values=[]
query3 = '''
SELECT Clarity.clarity,
    COUNT(Diamond.diamond_index) AS count
    FROM Diamond 
    INNER JOIN Clarity ON Diamond.clarity = Clarity.clarity
GROUP BY Clarity.clarity
ORDER BY count DESC
'''
cursor.execute(query3)

for row in cursor.fetchall():
    names.append (row[0])
    values.append(row[1])
scatter = go.Scatter (x = names, y = values)
scatter = py.plot([scatter],auto_open = True, file_name = "Plot3")



my_dboard = dash.Dashboard()
bar_id = fileId_from_url(bar)
pie_id =fileId_from_url(pie)
scatter_id = fileId_from_url(scatter)
box_1= {
    'type': 'box',
    'boxType': 'plot',
    'fileId': bar_id,
    'title': '1.Вивести категорії та загальну кількість діамантів, які входять до них.'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': pie_id,
    'title': '2.Вивести колір та % діамантів з таким кольором серед діамантів усіх кольорів.'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': scatter_id,
    'title': '3.Динаміка залежності прозорості діаманту від кількості діамантів, які мають таку прозорість.'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)


py.dashboard_ops.upload(my_dboard, 'db_Vika_lab2')


cursor.close()
connection.close()
