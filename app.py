import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# NASA API Key (Replace with your own API key)
NASA_API_KEY = "your_nasa_api_key"

@app.route('/')
def home():
    date = request.args.get('date', '')  # Get the date from query params
    if date:
        # Fetch data for the selected date
        url = f"https://api.nasa.gov/planetary/apod?date={date}&api_key={NASA_API_KEY}"
    else:
        # Fetch today's APOD
        url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    
    response = requests.get(url)
    if response.status_code != 200:
        return render_template('error.html', error="Failed to fetch data from NASA API.")
    
    data = response.json()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
