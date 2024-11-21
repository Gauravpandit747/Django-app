import requests

endpoint = "http://localhost:8000/api/"

response =requests.post(endpoint, json={"title":'Hello World'})
# print(response.text)
print(response.json())