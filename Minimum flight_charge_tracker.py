import requests
import datetime
from twilio.rest import Client

flight_api = "<YOUR flight_api>"
end_point = "https://api.sheety.co/<YOUR SHEETY API>/flightSearch/users"
tequila = "https://api.tequila.kiwi.com/locations/query"
flight_search = "https://api.tequila.kiwi.com/v2/search"
account_sid = "<YOUR account_sid>"
auth_token = "<YOUR auth_token>"


def convert_city(city):
    headers = {
        "apikey": flight_api,
    }

    para = {
        "term": city
    }

    short = requests.get(url=tequila, params=para, headers=headers)
    short = short.json()

    return short["locations"][0]["code"]


response1 = requests.get(url=end_point)
get_data = response1.json()

sheet_data = {data["city"]: convert_city(data["city"]) for data in get_data["city"]}
sheet_price = {data["city"]: data["lowestPrice"] for data in get_data["city"]}

data2 = datetime.datetime.today() + datetime.timedelta(days=2)
day2 = str(data2.date())
data180 = datetime.datetime.today() + datetime.timedelta(days=180)
day180 = str(data180.date())
data7 = datetime.datetime.today() + datetime.timedelta(days=7)
day7 = str(data7.date())
data28 = datetime.datetime.today() + datetime.timedelta(days=28)
day28 = str(data28.date())

for (key, items) in sheet_data.items():
    search = {
        "fly_from": "LON",
        "fly_to": items,
        "date_from": day2,
        "date_to": day180,
        "return_from": day7,
        "return_to": day28,
        "adults": 1,
        "children": 0,
        "curr": "GBP"
    }
    headers = {
        "apikey": flight_api,
    }

    response2 = requests.get(url=flight_search, params=search, headers=headers)
    search_data = response2.json()
    best_price = search_data["data"][0]["price"]
    if best_price < sheet_price[key]:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Your flight to {key} is at its lowest price of {best_price}, Book a ticket now",
            from_="<YOUR FROM>",
            to="<YOUR TO>"
        )
        print(message.status)
    else:
        print("high")
