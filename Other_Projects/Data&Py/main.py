import psycopg2 as pg2
conn = pg2.connect(database='dvdrental', user='postgres', password='Hossein513')
cur = conn.cursor()
cur.execute('SELECT * FROM film')
data = cur.fetchone()
print(data[2])
