from flask import Flask, Response

server = Flask(__name__)

@server.route("/give/<pi>/<pip>")
def piz(pi, pip):
    st = int(pi)
    end = int(pip)
    cur = st
    summ = 0

    while (cur <= end):
        cur += 1
        summ += cur
        res = {"str":str(summ)}

    return res
    
if __name__ == "__main__":
    server.run(use_reloader=True, port=3000)