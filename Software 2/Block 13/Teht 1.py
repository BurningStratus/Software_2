"""
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. 
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. 

Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. 

Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
"""

from flask import Flask, request, Response
import json

server = Flask(__name__)


@server.route("/alkuluku/<num>")
def onkoalkuluku(num):
    
    try:
        num = int(num)
    except:
        from random import randint
        num = randint(0, 10)


    dict_0 = {}
    isprime = True

    for i in range(2, num):
        if num % i == 0:
            isprime = False
            break

    return {"Number": num, "isprime": isprime}


if __name__ == "__main__":
    server.run(use_reloader = True, port = 3000)