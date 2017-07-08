import pymysql

class PoloDao:

    def __init__(self):
        self.db_conn = pymysql.connect("localhost", "root", "85ms3t", "first_schema")
        self.cursor = self.db_conn.cursor()
        self.db_conn.close()

    def insert(self,values):
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
           LAST_NAME, AGE, SEX, INCOME)
           VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        self.cursor.execute(sql)

    def executeCommand(self, command, values = None):
        self.openConnection()
        if(command == 'insert'):
            self.insert(values)

        self.closeConnection()

    def openConnection(self):
        self.db_conn = pymysql.connect("localhost", "root", "85ms3t", "first_schema")
        self.cursor = self.db_conn.cursor()

    def closeConnection(self):
        self.db_conn.close()