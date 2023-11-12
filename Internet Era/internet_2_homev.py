from flask import Flask, request, Response
import json
import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database='hr_manager',
    user='root',
    password='red_banana',
    autocommit=True
)

def sql_query(query):
    res_dic = {}
    cursor = connection.cursor()
    cursor.execute(query)
    response = cursor.fetchone()
    res_dic["query"] = response
    return res_dic
    

server = Flask(__name__)

@server.route("/")
def get_root():
    arg = "SHOW TABLES;"
    ress = sql_query(arg)
    print(ress)
    return ress

if __name__ == '__main__':
    server.run(use_reloader=True, host='127.0.0.1', port=3000)

'''
@server.route("/sql")
def get_data_sql():
    arg = "SHOW TABLES;"
    return sql_query(arg)
'''