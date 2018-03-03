import MySQLdb

db = MySQLdb.connect(host="webscrapper-instance.c2ay3hczfmtj.us-east-2.rds.amazonaws.com", 
			user="admin_webscrap", 
			passwd="password", 
			db="mlh_data")

cur = db.cursor()
cur.execute("Select * from test_table")

for row in cur.fetchall();
	print row[0]

db.close()

