import sqlite3
con = sqlite3.connect("test.db")

c = con.cursor()
res = c.execute("""SELECT * FROM person""")
print(res.fetchall())
res1 = c.execute("""SELECT * FROM address""")
print(res1.fetchall())
con.close()
