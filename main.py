import random

import requests

from flask import Flask, g, jsonify, render_template, request

app = Flask(__name__)


def nearby():
    fields = "photos,formatted_address,name"
    location = "5.5698567,-0.169646"
    keyword = "coffee shop"
    key = "key"
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?fields={}&location={}&radius=150000&keyword={}&key={}"
    url = url.format(fields, location, keyword, key)
    r = requests.get(url)   
    data = r.json()    
    results = data["results"]   
    places = []
    for result in results:
        try:
            photo_ref = result['photos'][0]['photo_reference']
            link = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={}&key={}".format(photo_ref, key)
            obj = {
                'name': result['name'],
                'photo': link
            }
            places.append(obj)
        except KeyError:
            continue
    return places

@app.route('/')
def hello_world():
    places = nearby()
    random.shuffle(places)
    return render_template('index.html', places=places)
