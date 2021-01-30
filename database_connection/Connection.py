
import pymysql
from pymysql import *

connection = pymysql.connect(host='den1.mysql1.gear.host',
    user='covidscrapping',
    password='Po42O588A!5!',
    db='covidscrapping',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    
try:
    with connection.cursor() as cursor:
        # Read a single record
        cursor.execute("SELECT * FROM example")
        row = cursor.fetchone()
        # Itero las tuplas:
        while row is not None:
            print(row)
            row = cursor.fetchone()

except:
    print("Ocurrió un error!")
finally:
    connection.close()
	