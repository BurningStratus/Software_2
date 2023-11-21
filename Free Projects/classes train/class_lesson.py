from flask import Flask, request, Response, render_template
import json

server = Flask(__name__)

# http://127.0.0.1:3000/jacket
@server.route("/<name>")
def sup_bitches(name):
    return render_template('html_js.html', name=name)

# http://127.0.0.1:3000/
@server.route("/")
def get_root():
    return render_template('html_js.html')

# http://127.0.0.1:3000/old_notation/3
@server.route('/old_notation/<arg>')
def multiply(arg):
    resp = {
    'velka': int(arg) * int(arg)
    }
    resp = json.dumps(resp)
    return render_template('html_js.html', name=resp)

# http://127.0.0.1:3000?arg=3
@server.route('/new_notation') # type: ignore
def mutiplly():
    arg = request.args.get("arg")
    
    try:
        arg = int(arg) # type: ignore
    except:
        return json.dumps({"req": 'bad request'})
    
    res = {
        arg: arg * arg
    }
    return render_template('html_js.html', name=json.dumps(res))
    

if __name__ == '__main__':
    server.run(use_reloader=True, port=3000)