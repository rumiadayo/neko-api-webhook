import json
import requests
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1199650770715426846/0BZFkILKH1YOZ7qfNzVJzS70EAQaBGSnQp5GnPSRZqXkg6Ni0rMUYsMZWM_oayAwFhAO"

while True:
    resp = requests.get("https://nekos.best/api/v2/neko")
    data = resp.json()
    link = data["results"][0]["url"]
    artist = data["results"][0]["artist_name"]
    payload = {
    "username"      : f"{artist}",
    "content"       : f"{link}",
    "avatar_url"    : f"{link}",
    }
    res = requests.post( WEBHOOK_URL, json=payload )
    time.sleep(1)
