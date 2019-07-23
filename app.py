rom flask import Flask
import urllib.request, json

app = Flask(__name__)

@app.route('/')

def print_nasa_data();
 with urllib.request.urlopen(https://api.nasa.gov/planetary/apod?api_key=Vg0VbaeecjP5l8HWudpPzpmdOIeG7FeQXbcknic1) as urllib:
        data = json.loads(url.read())

        return data

if __name__ == '__main__':
    app.run()