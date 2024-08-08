from opencage.geocoder import OpenCageGeocode
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from datetime import datetime
import aiohttp
import asyncio
import random



import asyncio

async def geocode(location: str):
    key = '5e6d2cba3c80477585b1d89088aa0907'
    geocoder = OpenCageGeocode(key)
    results = await asyncio.to_thread(geocoder.geocode, location + ', Nigeria')

    if results:
        latitude = results[0]['geometry']['lat']
        longitude = results[0]['geometry']['lng']
        return {"lat": latitude, "long": longitude}
    return "Geocoding failed."

# Running the async function and printing the result
#result = asyncio.run(geocode("oyo"))
#lat, long = result["lat"],result["long"]
#print(lat,long)


# Setup the Open-Meteo API client with cache and retry on error
# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)



import requests
from datetime import datetime

def fetch_weather_data(lat, long):
    # Get the current date in the required format (YYYY-MM-DD)
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Setup the URL and parameters for the request
    url = "https://climate-api.open-meteo.com/v1/climate"
    params = {
        "latitude": lat,
        "longitude": long,
        "start_date": current_date,
        "end_date": current_date,
        "models": "FGOALS_f3_H",
	    "timezone": "Africa/Cairo",
        "daily": ["cloud_cover_mean", "shortwave_radiation_sum"]
    }

    # Initialize an empty dictionary to store the required data
    data_dict = {}

    # Synchronously request the weather data
    response = requests.get(url, params=params)
    result = response.json()



    # Process the response for the specific day
    if result:
        data_dict["latitude"] = params["latitude"]
        data_dict["longitude"] = params["longitude"]

        daily_data = result.get('daily', {})

        daily_cloud_cover_mean = daily_data.get('cloud_cover_mean', [])
        daily_shortwave_radiation_sum = daily_data.get('shortwave_radiation_sum', [])

       

        # Since the request is for a single day, get the first entry of each array
        if daily_cloud_cover_mean and daily_shortwave_radiation_sum:
            data_dict["cloud_cover_mean"] = daily_cloud_cover_mean[0]
            data_dict["shortwave_radiation_sum"] = daily_shortwave_radiation_sum[0]

    # Return the resulting dictionary
    data_dict['mixing_ratio_difference'] = random.random()
    return data_dict


'''['cloud_fraction_current', 'radiation_current', 'latitude', 'longitude',
       'nox_mixing_ratio_difference']
'''
async def fetch_weather_data_async(latitude, longitude):
    loop = asyncio.get_running_loop()
    data_dict = await loop.run_in_executor(None, fetch_weather_data, latitude, longitude)
    print(data_dict)
    data_list = [[data_dict["cloud_cover_mean"], data_dict["shortwave_radiation_sum"], data_dict["latitude"], data_dict["longitude"]]]
    
    return data_list

# data = asyncio.run(fetch_weather_data_async(4.5, 5.4))
# print(data)
