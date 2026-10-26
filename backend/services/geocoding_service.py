import requests
import os

def fetch_geocoding_data(entity):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={entity}&key={os.getenv('OPENCAGE_API_KEY')}"
    res = requests.get(url)
    if res.status_code == 200:
        results = res.json().get("results", [])
        if results:
            return {
                "name": entity,
                "lat": results[0]["geometry"]["lat"],
                "lng": results[0]["geometry"]["lng"],
            }
    return None
