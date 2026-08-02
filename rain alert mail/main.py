import os
from dotenv import load_dotenv
import smtplib
import requests
load_dotenv()
dict={
    "lat":17.709789,
    "lon":83.160919,
    "appid": os.getenv("API_KEY"),
    "cnt":4,
}

response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=dict)
response.raise_for_status()
weather_data=response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<600:
        will_rain=True
if will_rain:
    with smtplib.SMTP ("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user="santoshreddy2357@gmail.com",password=os.getenv("PASSWORD"))
        connection.sendmail(from_addr="santoshreddy2357@gmail.com",to_addrs="santoshreddy2357@gmail.com",msg="Subject:it might rain santosh\n\n take an umbrella with u !")

