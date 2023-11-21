# requests. do a request to a chuck norris API

import requests
'''
req = 'https://chucknorrisapi.io/jokes/random'
response = requests.get(req).json()
print(response["value"])
'''
# flask

from flask import Flask, request, Response
import json

server = Flask(__name__)

@server.route("/")
def get_root():
    return "helo"

#modern arg notation

@server.route("/get_sum/")
def get_sum():
    args = request.args
    integ = args.get("int1")
    integ2 = args.get("int2")
    try:
        num1, num2 = int(integ), int(integ2)
        status = 200
        response = {
            "request": f"sum {num1} & {num2}",
            "status": status,
            "result": str(num1 + num2)}
        
        response = json.dumps(response)

    except ValueError:
        status = 400
        response = {
            "request": "sum",
            "status": status,
            "response": "bad args"
        }

        response = json.dumps(response)
    
    return Response(response= response, status= status, mimetype= "application/json")

if __name__ == '__main__':
    server.run(use_reloader= True, port= 3000)