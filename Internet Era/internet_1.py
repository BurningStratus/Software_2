from flask import Flask, request, Response
import json

server = Flask(__name__)
#print(__name__)

@server.route("/")
def get_root():
    return "'internet_era'"


# http://127.0.0.1:3000/dir?name=MMM&age=19
@server.route("/dir")
def get_hello():
    print(request.args)
    name = request.args.get("name")
    age = request.args.get("age")
    return f"directory or sumthin'. {name}, {age}"

# http://127.0.0.1:3000/dir/MMM
@server.route("/dir_another/<name>/<age>")
def get_not_hello(name, age):
    print(request.args)
    # name = request.args.get("name")
    return f"directory or sumthing. And fuck you, {name}, {age}"


@server.route("/funny")
def calculate():
    f_num, s_num = request.args.get("number_1"), request.args.get("number_2")
    return f"{int(f_num)+int(s_num)}"

# http://127.0.0.1:3000/dir/num1
# ex. res: 'num1: 5, res: 25'
@server.route("/multiply/<num>")
def multiply(num):
    num = int(num)
    result = num * num
    response = {"input_num": num, "result": result}
    return response


@server.route("/calc/<num>")
def calc(num):
    try:
        num = int(num)

    except ValueError:
        response_data = {"input_num": num, "result": "are you fucking retarded? only numbers allowed"}
        response_data = json.dumps(response_data)
        response = Response(response=response_data, status=400, mimetype="application/json")
        return response


    if 100 > num > 0:
        response = {"input_num": num, "result": num ** 2}
        return response
    else:
        response_data = {"input_num": num, "result": "result out of bounds"}
        response_data = json.dumps(response_data)
        response = Response(response=response_data, status=400, mimetype="application/json")
        return response


if __name__ == '__main__':
    server.run(use_reloader=True, port=3000)

