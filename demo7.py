import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test_demo_7.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('CREATE TABLE COMPANY(ID INT PRIMARY KEY     NOT NULL,NAME           TEXT    NOT NULL,AGE            INT     NOT NULL,ADDRESS        CHAR(50),SALARY         REAL);')


cursor.close()
conn.commit()
conn.close()