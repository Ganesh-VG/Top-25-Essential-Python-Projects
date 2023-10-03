import requests
import datetime

api_id = "<YOUR api_id>"
api_key = "<YOUR api_key>"
end_point = " https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("Tell me which exercises you did?")

params = {
 "query": exercise,
 "gender": "male",
 "weight_kg": 77,
 "height_cm": 171,
 "age": 27
}

headers = {
    "x-app-id": api_id,
    "x-app-key": api_key,
    "x-remote-user-id": "0",
}

response = requests.post(url=end_point, json=params, headers=headers)
data = response.json()
print(data)

sheety_api = "https://api.sheety.co/<SHEETY API>/myWorkout/workout"
date_n = datetime.datetime.now()
date = date_n.strftime("%Y/%m/%d")
time = date_n.strftime("%H:%M:%S")

for a in range(len(data["exercises"])):
    workouts = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": data["exercises"][a]["user_input"],
            "duration": data["exercises"][a]["duration_min"],
            "calories": data["exercises"][a]["nf_calories"]
        }
    }
    response = requests.post(url=sheety_api, json=workouts)


print(response.text)
print(response.status_code)