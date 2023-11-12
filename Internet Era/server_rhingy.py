import requests


def response_handler(res_server):
    
    for show in res_server:
        if show['score'] > 0.5:
            print()
            print(show['show']['name'])
            print(show['score'])
            for genre in show['show']['genres']:
                print(genre)
            
            return None


query = input(f"Query:> ")
request = f'https://api.tvmaze.com/search/shows?q={query}'


try:
    response = requests.get(request).json()
    response_handler(response)
except requests.exceptions.RequestException as error_exception:
    print("sumthin' broke :( ")
    print(error_exception)


# print(response)


