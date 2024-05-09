from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city):
    api_key = "bf4fb215230a8becfedafaff7d363234"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        if weather_data["cod"] == 200:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            pressure = weather_data['main']['pressure']
            description = weather_data['weather'][0]['description']
            return render_template('index.html', city=city, temperature=temperature,
                                   humidity=humidity, description=description, pressure=pressure)
        else:
            error_message = "City not found. Please try again."
            return render_template('index.html', error_message=error_message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
