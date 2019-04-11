# Sqlite3を使うテストモジュール
import sqlite3

con = sqlite3.connect('test.db')
# con = sqlite3.connect('db.sqlite3')
cursor = con.cursor()
# cursor.execute('DROP TABLE IF EXISTS data_set')
# cursor.execute('CREATE TABLE data_set(id,name,date)')

# sql = 'INSERT INTO data_set(id,name,date) VALUES(?,?,?)'
# cursor.execute(sql, (2, 'takeda', 19841023))
# con.commit()

cursor.execute('SELECT * FROM data_set ORDER BY id DESC')
# cursor.execute('SELECT * FROM sqlite_master WHERE type="table"')
for x in cursor.fetchall():
    print(x)
# data = cursor.fetchall()
# print(data)

con.close()
