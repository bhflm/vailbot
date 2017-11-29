import requests, datetime, tweepy, json
from keys import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



def tweet():
    #LAT Y LONG DE VAIL
    url = "https://api.darksky.net/forecast/"+darksky_api_key+"/39.640264, -106.374195"
    json_data = requests.get(url).json()
    high = str(json_data['daily']['data'][0]['temperatureMax'])
    low = str(json_data['daily']['data'][0]['temperatureMin'])
    maxima = "{0:.2f}".format((float(high) - 32)*5/9)
    minima = "{0:.2f}".format((float(low) - 32)*5/9)

    mensaje = "@germibh Pronostico en [VAIL,CO]: Maxima: " + str(maxima) + " | Minima: " + str(minima) + " |"

    api.update_status(mensaje)


tweet()
