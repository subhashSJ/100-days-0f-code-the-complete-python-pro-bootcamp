import requests
import datetime as dt
from dotenv import load_dotenv
import os

GENDER = "Male"
WEIGHT_KG = "58"
HEIGHT_CM = "157.5"
AGE = "24"

load_dotenv()

headers = {
    'x-app-id': os.environ['API_ID'],
    'x-app-key': os.environ['API_KEY']
}

query = input("Tell me which exercises you did: ")

body = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(
    url=os.environ['NUTRITIONIX_ENDPOINT'], json=body, headers=headers)
response.raise_for_status()
exercises = response.json()['exercises']

rows = []
for exercise in exercises:
    row = {}
    row["Date"] = str(dt.datetime.now().date())
    row["Time"] = str(dt.datetime.now().time())
    row['Exercise'] = exercise['user_input']
    row['Duration'] = exercise['duration_min']
    row['Calories'] = exercise['nf_calories']

    rows.append(row)

for row in rows:
    row_body = {
        "workout": {
            "date": row['Date'],
            "time": row['Time'],
            "exercise": row['Exercise'].title(),
            "duration": str(row['Duration']),
            "calories": str(row['Calories']),
        }
    }

    headers = {
        "Authorization": f"Basic {os.environ['TOKEN']}="
    }

    response = requests.post(
        url=os.environ['SHEET_ENDPOINT'], json=row_body, headers=headers)
    response.raise_for_status()
