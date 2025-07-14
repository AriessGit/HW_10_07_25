import sqlite3

conn = sqlite3.connect('10_07_25.db') 
cursor = conn.cursor()
conn.row_factory = sqlite3.Row

def join_type_func(requested_join):
    cursor.execute(requested_join)
    for row in cursor.fetchall():
        print(dict(row))

inner_join = '''SELECT passengers.*, taxis.driver_name, taxis.car_type
            FROM passengers JOIN taxis ON passengers.taxi_id = taxis.id;'''

left_join ='''SELECT p.*, t.driver_name , t.car_type FROM passengers p  
            LEFT join taxis t ON p.taxi_id = t.id'''

full_join = '''SELECT p.*, t.driver_name , t.car_type FROM passengers p  
            LEFT join taxis t ON p.taxi_id = t.id WHERE p.taxi_id is NULL'''

cross_join = '''SELECT p.*, t.driver_name, t.car_type FROM passengers p  
            LEFT JOIN taxis t ON p.taxi_id = t.id WHERE t.id IS NULL'''


joins = [inner_join, left_join, full_join, cross_join]

for join in joins:
    print(join)
    join_type_func(join)


conn.close()


