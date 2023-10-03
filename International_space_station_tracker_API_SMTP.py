import requests
import datetime as dt
import smtplib

def iss_close():
    if 9 < iss_latitude < 20 and 69 < iss_longitude < 80:
        return True


def night():
    if sunset < hour or hour < sunrise:
        return True


my_lat = "<YOUR LATITUDE>"
my_lng = "<YOUR LONGITUDE>"
my_email = "<YOUR EMAIL>"
password = "<YOUR PASSWORD GENERATED SPECIALLY FOR SMTP LIBRARY>"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_latitude = data["iss_position"]["latitude"]
iss_longitude = data["iss_position"]["longitude"]

iss_position = (iss_latitude, iss_longitude)

print(iss_position)

parameters = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0,
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

sunrise = int(sunrise)+5
sunset = int(sunset)+5

ti_hr = dt.datetime.now()
hour = ti_hr.hour

if iss_close() is True and night() is True:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="<TO EMAIL>",
                            msg="Subject:International Space Station Alert!\n\nInternational space station "
                                "is in your visible range. Just take a look at dark sky")