
# 2 classes for each type of APIs. SQL, Chuck Norris API
# Chuck norris calls API for a phrase
# phrase is written to SQL DB.

import requests
import mysql.connector as mysql
from datetime import datetime


class SQL:

    host = '127.0.0.1'
    def __init__(self, user, pword, database):
        self.user = user
        self.pword = pword
        self.database = database
        self.connection = mysql.connect(
            host = SQL.host,
            port = 3306,
            database = self.database,
            user = self.user,
            password = self.pword,
            autocommit = True
        )
    
    def show_tables(self):
        sql_command = 'SHOW TABLES;'
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute(sql_command)
        
        res = cursor.fetchall()
        resp_string = f'TABLES IN {self.database}:\n'

        for all in res:
            resp_string += "> " + all[0] + "\n"

        return resp_string
    
    def describe(self, table):
        sql_command = f'DESC {table};'
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute(sql_command)
        
        res = cursor.fetchall()
        resp_string = f'ROWS IN {table}:\n'

        for all in res:
            resp_string += "> " + all[0] + "  ->  " + all[1] + "\n"

        return resp_string

    def alter_table(self, table, data, time):
        sql_command = f"INSERT INTO {table} VALUES ('{data}', {time});"
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute(sql_command)
        print(cursor.fetchwarnings())

def request_api():
    now = datetime.now()

    date_string = f'{now.month}{now.day}{now.hour}'
    date_int = int(date_string)
    resp = requests.get('https://api.chucknorris.io/jokes/random').json()

    return resp["value"], date_int


chuck_prikol = SQL('root', 'cr1ng3', 'chuck_prikol')
value = request_api()[0]
time = request_api()[1]

print(value, type(value))
print(time, type(time))

chuck_prikol.alter_table('prikol', value, time)
chuck_prikol.describe('prikol')