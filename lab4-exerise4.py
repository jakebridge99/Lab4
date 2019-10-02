import sqlite3


dbconnect = sqlite3.connect("my.db");

dbconnect.row_factory = sqlite3.Row;

cursor = dbconnect.cursor();

dbconnect.commit();

cursor.execute('SELECT * FROM SENSORS WHERE zone= "kitchen"' );

for row in cursor:
	print(row['sensorid'],row['type'],row['zone']);
print("\n");
cursor.execute('SELECT * FROM SENSORS WHERE type = "door"');

for row in cursor:
	print(row['sensorid'],row['type'], row['zone']);
dbconnect.close();
