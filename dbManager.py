import sqlite3

conn = sqlite3.connect('Ipee.db')
c = conn.cursor()

def create_tables():
	c.execute('CREATE TABLE IF NOT EXISTS HISTORY(user_id INTEGER, lock_id INTEGER, place_id INTEGER, balance INTEGER, date date, time timestamp)')
	
def insert():
	#c.execute("INSERT INTO HISTORY (user_id, lock_id, place_id, balance, date, time) VALUES (?,?,?,?,?,?)")
	c.execute("INSERT INTO HISTORY (user_id, lock_id, place_id, balance, date, time) VALUES (1,1,2,3,'2017-08-03','10:48:00')")
	conn.commit()
	c.close()
	conn.close()
	
def read_from_db():
	c.execute('SELECT * FROM HISTORY')
	for row in c.fetchall():
		print(row)
		
create_tables()		