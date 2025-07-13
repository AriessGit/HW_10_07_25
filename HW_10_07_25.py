import sqlite3

conn = sqlite3.connect('check.db') 
cursor = conn.cursor()

print('''SELECT passengers.*, taxis.driver_name, taxis.car_type
FROM passengers
JOIN taxis ON passengers.taxi_id = taxis.id;''')

cursor.execute('''
SELECT passengers.*, taxis.driver_name, taxis.car_type
FROM passengers
JOIN taxis ON passengers.taxi_id = taxis.id;
''')
for row in cursor.fetchall():
    print(dict(row))


print('''SELECT p.*, t.driver_name , t.car_type FROM passengers p  
LEFT join taxis t ON p.taxi_id = t.id''')

cursor.execute('''SELECT p.*, t.driver_name , t.car_type FROM passengers p  
LEFT join taxis t ON p.taxi_id = t.id''')
for row in cursor.fetchall():
    print(dict(row))

print('''SELECT p.*, t.driver_name , t.car_type FROM passengers p  
LEFT join taxis t ON p.taxi_id = t.id WHERE p.taxi_id is NULL''')

cursor.execute('''SELECT p.*, t.driver_name , t.car_type FROM passengers p  
LEFT join taxis t ON p.taxi_id = t.id WHERE p.taxi_id is NULL''')
for row in cursor.fetchall():
    print(dict(row))

print('''SELECT p.*, t.driver_name , t.car_type FROM passengers p  
FULL join taxis t ON p.taxi_id = t.id''')

cursor.execute('''SELECT p.*, t.driver_name , t.car_type FROM passengers p  
FULL join taxis t ON p.taxi_id = t.id''')
for row in cursor.fetchall():
    print(dict(row))


print('''SELECT p.*, t.driver_name , t.car_type FROM passengers p  
CROSS join taxis t ''')

cursor.execute('''SELECT p.*, t.driver_name , t.car_type FROM passengers p  
CROSS join taxis t ''')
for row in cursor.fetchall():
    print(dict(row))




conn.close()


