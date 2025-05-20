import os
import requests
from datetime import datetime, timedelta

def fetch_and_save_csv():
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    property_id = "755178"
    api_key = os.getenv("LOD_API_KEY")

    endpoints = {
        "currently_staying": f"https://api.lodgify.com/v1/bookings/export/csv/currently-staying?propertyId={property_id}&date={tomorrow}",
        "next_arrivals": f"https://api.lodgify.com/v1/bookings/export/csv/next-arrivals?propertyId={property_id}&date={tomorrow}",
        "next_departures": f"https://api.lodgify.com/v1/bookings/export/csv/next-departures?propertyId={property_id}&date={tomorrow}"
    }

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    for name, url in endpoints.items():
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            file_path = f"{name}_{tomorrow}.csv"
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"✔ Zapisano: {file_path}")
        else:
            print(f"❌ Błąd pobierania {name}: {response.status_code} - {response.text}")

if __name__ == "__main__":
    fetch_and_save_csv()
