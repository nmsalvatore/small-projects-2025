#!/usr/bin/env python3

import os
import requests

from dotenv import load_dotenv


load_dotenv()

ZIP_CODE: int = os.getenv("ZIP_CODE")
API_KEY: str | None = os.getenv("TOMORROW_API_KEY")

if API_KEY is None:
    raise ValueError("Could not find enviroment variable API_KEY")

url = f"https://api.tomorrow.io/v4/weather/forecast?timesteps=1d&units=imperial&location={ZIP_CODE}&apikey={API_KEY}"

headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}

response = requests.get(url, headers=headers)
data = response.json()

print([day["values"]["precipitationProbabilityMax"] for day in data["timelines"]["daily"]])
