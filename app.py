from flask import Flask, Response, jsonify
import json
import requests

app = Flask(__name__) # . is current directory

data_url = "https://raw.githubusercontent.com/hvo/datasets/master/nyc_restaurants_by_cuisine.json"

def loadData():
    return json.loads(requests.get(data_url).content)

data = loadData()

with app.open_resource('static/chart.json', 'r') as f: # read the json file as dict
    chart = json.load(f)

@app.route('/vis/<ZipCode>')
def visualize(ZipCode=None):
    chart['data']['url'] = '/data/{}'.format(ZipCode)
    return jsonify(chart)

@app.route('/data/<ZipCode>')
def get_data(ZipCode=None):
    zipcodes = []
    for d in data:
        zipcodes.append({
        'cuisine': d['cuisine'],
        'total': d['perZip'].get(ZipCode,0)
        })
    zipcodes = sorted(zipcodes, key=lambda d: d['total'], reverse=True) # bcs sort in altair doesn't work
    return jsonify(zipcodes)

# equal to
# return sorted([dict(cuisine = d['cuisine'],
#                       total = d['perZip'].get(zipcode)) for d in data],
#                       key=lambda d: d['total'], reverse=True)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(port=8800, debug=True)
