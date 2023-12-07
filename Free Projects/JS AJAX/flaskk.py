from flask import Flask, Request, Response
from flask_cors import CORS
import json


server = Flask(__name__)
cors = CORS(server)
# server.config["CORS_HEADERS"] = 'Content-Type'


@server.route('/add/<num1>/<num2>')
def calc(num1, num2):
    sum = int(num1) + int(num2)
    print(sum)
    response = {"sum":sum}
    response = json.dumps(response)
    return Response(mimetype='application/json', response=response)

if __name__ == "__main__":
    server.run(use_reloader=True, port=3000)