import  pymysql

class TestingDB:

    def __init__(self):
        pass


db_conn = pymysql.connect("localhost","root","85ms3t","first_schema" )
x = db_conn.cursor()
try:
   x.execute("""INSERT INTO first_table VALUES (%s,%s,%s)""",(1,2,3))
   db_conn.commit()
except:
    db_conn.rollback()

db_conn.close()

print("bla")
