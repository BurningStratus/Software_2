import requests

responses = []

def req_chuck_norris(arg, whereto):
    
    for times in range(arg):
        res = requests.get('https://api.chucknorris.io/jokes/random').json()
        whereto.append(res["value"])
    
    return whereto

req_chuck_norris(10, responses)

for citate in responses:
    print(f" {citate} \n")