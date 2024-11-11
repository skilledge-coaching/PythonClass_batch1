import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
print(response)

if response.status_code == 200:
    joke = response.json()
    print(joke)

    print("here's a joke for you")
    print(joke["setup"])
    print(joke["punchline"])
else:
    print("failed to retrieve a joke. Try again later")