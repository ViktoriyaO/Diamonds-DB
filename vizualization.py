import cx_Oracle
import plotly.offline as py
import plotly.graph_objs as go
import re
import plotly.dashboard_objs as dashboard

def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

connection = cx_Oracle.connect("sys", "Xmaswithnk2018", "localhost:1521/xe")
cursor = connection.cursor()

""" create plot 1   Вивести категорії та загальну кількість діамантів, які входять до них."""
cursor.execute("""
SELECT cut, COUNT(diamond_index) AS count
    FROM Diamond
GROUP BY cut
ORDER BY count DESC;""")
cut = []
count =[]

for row in cursor:
    print("Categories of diamonds: ",row[1]," and count of diamonds: ",row[2])
    cut += [row[0]+""+row[1]]
    count +=[row[2]]

data = [go.Bar(
            x=cut,
            y=count
    )]

layout = go.Layout(
    title='Categories and count of diamonds',
    xaxis=dict(
        title='Categories',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Count of diamonds',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
categories_count_diamonds = py.plot(fig, filename='categories-count-diamonds')


""" create plot 2   Вивести колір та % діамантів з таким кольором серед діамантів усіх кольорів."""
cursor.execute("""
SELECT 
    color, 
    ROUND(COUNT(diamond_index)*100/t.count, 2) AS persent
    FROM Diamond,
    (SELECT COUNT(diamond_index) AS count
    FROM Diamond)t   
GROUP BY  color,
        t.count;
""");
color = []
persent = []

for row in cursor:
    print("Colors of diamonds ", row[1] + " id: (" + row[0], ") and count of diamonds with this color: ", row[2])
    color += [row[1] + " " + row[0]]
    persent += [row[2]]

pie = go.Pie(labels=color, values=persent)
color_count_diamonds = py.plot([pie], filename='color-count-diamonds')


""" create plot 3   Динаміка залежності прозорості діаманту від кількості діамантів, які мають таку прозорість."""
cursor.execute("""
SELECT Clarity.clarity,
    COUNT(Diamond.diamond_index) AS count
    FROM Diamond 
    INNER JOIN Clarity ON Diamond.clarity = Clarity.clarity
GROUP BY Clarity.clarity
ORDER BY count DESC;
""")
clarity = []
count = []

for row in cursor:
    print("Clarity ", row[0], " count of diamonds: ", row[1])
    clarity += [row[0]]
    count += [row[1]]

clarity_count_diamonds = go.Scatter(
    x=clarity,
    y=count,
    mode='lines+markers'
)
data = [clarity_count_diamonds]
clarity_count_diamonds_url = py.plot(data, filename='Clarity by count of diamonds')


"""--------CREATE DASHBOARD------------------ """

my_dboard = dashboard.Dashboard()

categories_count_diamonds_id = fileId_from_url(categories_count_diamonds)
color_count_diamonds_id = fileId_from_url(color_count_diamonds)
clarity_count_diamonds_id = fileId_from_url(clarity_count_diamonds_url)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': categories_count_diamonds_id,
    'title': 'Categories and count of diamonds'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': color_count_diamonds_id,
    'title': 'Color and count of diamonds'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': clarity_count_diamonds_id,
    'title': 'Clarity by count of diamonds'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'My First Dashboard with Python')



