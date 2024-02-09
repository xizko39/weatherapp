from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("API_KEY")

@app.route('/weather/<city>')
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    return jsonify({
        "location": city.capitalize(),
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["main"]
    })

if __name__ == '__main__':
    app.run(debug=True)
