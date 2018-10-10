from flask import Flask, request, render_template, g, jsonify
import requests

app = Flask(__name__)


def nearby():
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=150000&keyword=cofee&key=AIzaSyAfBOVn3dRaeJ78FgqLNsWFec84oIe4e6A'
    r = requests.get(url)   
    data = r.json()    
    places = data["results"]   
    data = []
    for place in places:
        try:
            photo_ref = place['photos'][0]['photo_reference']
            link = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={}&key={}".format(photo_ref, 'AIzaSyAfBOVn3dRaeJ78FgqLNsWFec84oIe4e6A')
            obj = {
                'name': place['name'],
                'photo': link
            }
            data.append(obj)
        except KeyError:
            continue
    return data

@app.route('/')
def hello_world():
    places = nearby()
    return render_template('index.html', places=places)



