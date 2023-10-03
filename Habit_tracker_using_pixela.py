import requests
import datetime


username = "YOUR USERNAME"
token = "YOUR TOKEN"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

graph_add = f"{pixela_endpoint}/{username}/graphs/graph1"

today = datetime.datetime.now()
yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
add_data = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "25"
}

graph_delete = f"{pixela_endpoint}/{username}/graphs/graph1/20230924"

new_pixel_data = {
    "quantity": "17"
}

headers = {
    "X-USER-TOKEN": token
}

response = requests.post(url=graph_delete, json=new_pixel_data, headers=headers)
print(response.text)
