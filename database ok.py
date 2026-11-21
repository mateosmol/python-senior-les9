import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS first_table (name TEXT);")

# cur.execute("INSERT INTO first_table (name) VALUES ('Nick')")
# cur.execute("INSERT INTO first_table (name) VALUES ('Anna')")
# cur.execute("INSERT INTO first_table (name) VALUES ('Tom')")
# connection.commit()

# cur.execute("SELECT rowid, name FROM first_table WHERE rowid=2;")
# print(cur.fetchall())

# cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=2;")
# connection.commit()

# cur.execute("SELECT rowid, name FROM first_table WHERE rowid=2;")
# print(cur.fetchall())

# cur.execute("DELETE FROM first_table WHERE rowid=6;")
# cur.execute("DELETE FROM first_table WHERE rowid=5;")
# cur.execute("DELETE FROM first_table WHERE rowid=4;")
# connection.commit()

cur.execute("SELECT rowid, name FROM first_table;")
print(cur.fetchall())

connection.close()