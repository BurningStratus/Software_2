"""
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa. 
Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. 

Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. 
Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
"""

from flask import Flask, Response
import mysql.connector
import json
########################
# remember to password!
username = 'root'
password = 
########################
sql_connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = username,
    password = password,
    autocommit = True
)
server = Flask(__name__)
#########################


# esimerkki pyynnöstä: http://127.0.0.1:3000/kenttä/EFHK
@server.route("/kenttä/<icao>")
def get_munic(icao):
    sql = f'SELECT ident, name, municipality FROM airport WHERE ident = "{icao}";'
    
    cursor = sql_connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) <= 0:
        response_data = {"requested icao": icao, "result": f"Empty set. Check spelling:> {icao}"}
        response_data = json.dumps(response_data)
        response = Response(response=response_data, status=400, mimetype="application/json")
        return response

    response_data = {"ICAO": result[0][0], "Name": result[0][1], "Municipality": result[0][2]}
    response_data = json.dumps(response_data)
    response = Response(response=response_data, status=200, mimetype="application/json")
    return response

if __name__ == "__main__":
    server.run(use_reloader = True, port = 3000)