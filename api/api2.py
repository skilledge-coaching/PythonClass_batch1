import requests

url = "https://api.adviceslip.com/advice"

response = requests.get(url)

print(response)

if response.status_code == 200:
    advice = response.json()
    print("Advice")
    print(advice["slip"]["advice"])
    # print(advice)
else:
    print("Failed to get data")