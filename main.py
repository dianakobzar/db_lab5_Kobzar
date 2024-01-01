import psycopg2
import matplotlib.pyplot as plt

username = 'kobzardiana'
password = '123'
database = 'db_lab3'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE VIEW PriceMerc AS
SELECT price, mers_class
FROM mercedes
GROUP BY price, mers_class;
'''
query_2 = '''
CREATE VIEW FuelTypeMerc AS
SELECT fuelType, COUNT(*) as carCount
FROM Mercedes
JOIN fuel ON Mercedes.fuelType_id = fuel.fuelType_id
GROUP BY fuelType;
'''
query_3 = '''
CREATE VIEW PriceDependency AS
SELECT engine.engineSize, Mercedes.price
FROM engine
JOIN Mercedes ON engine.engineSize_id = Mercedes.engineSize_id
ORDER BY engine.engineSize;
'''
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    cur.execute('DROP VIEW IF EXISTS PriceMerc')
    cur.execute(query_1)
    cur.execute('SELECT * FROM PriceMerc;')
    price = []
    mers_class = []

    for row in cur:
        price.append(row[0])
        mers_class.append(row[1])

    x_range = range(len(mers_class))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1,3)
    bar = bar_ax.bar(x_range, price, label='mers_class')
    bar_ax.bar_label(bar, label_type='center')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(mers_class, ha='left')
    bar_ax.set_ylabel('Ціна, €')
    bar_ax.set_title('Ціни на мерседеси')
    figure.text(0.25, 0.05, 'Клас мерседесів', ha='center', va='center', fontsize=10)

    cur.execute('DROP VIEW IF EXISTS FuelTypeMerc')
    cur.execute(query_2)
    cur.execute('SELECT * FROM FuelTypeMerc;')
    fuelType = []
    carCount = []

    for row in cur:
        fuelType.append(row[0])
        carCount.append(row[1])

    x_range = range(len(carCount))
    pie_ax.pie(carCount, labels=fuelType, autopct='%1.1f%%')
    pie_ax.set_title('Види палива по кількостях')

    cur.execute('DROP VIEW IF EXISTS PriceDependency')
    cur.execute(query_3)
    cur.execute('SELECT * FROM PriceDependency;')
    engineSize = []
    price = []

    for row in cur:
        price.append(row[0])
        engineSize.append(row[1])

    mark_color = 'blue'
    graph_ax.plot(price, engineSize, color=mark_color, marker='o')

    for qnt, engineSize in zip(price, engineSize):
        graph_ax.annotate(engineSize, xy=(qnt, engineSize), color=mark_color,
                          xytext=(7, 2), textcoords='offset points')

    graph_ax.set_xlabel('Ціна')
    graph_ax.set_ylabel("Об'єм двигуна")
    graph_ax.set_title("Графік залежності ціни від об'єму двигуна")

plt.show()

