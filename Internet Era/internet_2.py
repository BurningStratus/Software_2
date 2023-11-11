from flask import Flask, request, Response
import mysql.connector

mariadb_sql = mysql.connector.connect(
    host = '127.0.0.1' ,
    port = 3306 ,
    database = 'flight_game' ,
    user = 'root' ,
    password = 'cr1ng3' ,
    autocommit = True
)

server = Flask(__name__)

@server.route("/")
def initial():
    routes = {
        1: "/",
        2: "/<sql query>",
        3: "None for now",
    }
    return routes


@server.route("/<sql_query>")
def sql_command(sql_query):
    cursor = mariadb_sql.cursor()
    cursor.execute(sql_query)
    response = cursor.fetchall()

    return response





if __name__ == '__main__':
    server.run(use_reloader = True, port = 3000)