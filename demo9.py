import sqlite3

conn = sqlite3.connect('test_demo_7.db')
cursor = conn.cursor()
cursor.execute( 'select * from COMPANY' )
values = cursor.fetchall()
print(values)
cursor.close()
conn.commit()
conn.close()