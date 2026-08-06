import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

GENDER="male"
WEIGHT=62
HEIGHT=175
AGE=20

base_endpoint="https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
exercise_text=input("what  excercise are u doing now :")
parameters={
    "query":exercise_text,
    "gender":GENDER,
    "weight": WEIGHT,
    "height":HEIGHT,
    "age":AGE
}
headers={
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("API_KEY")
}

response=requests.post(url=base_endpoint,json=parameters,headers=headers)
result=response.json()

today_date=datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

exercise = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]




today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        os.getenv("sheety_endpoint"),
        json=sheet_inputs,
        auth=("santosh", "12345678")
    )
    print(sheet_response.text)


