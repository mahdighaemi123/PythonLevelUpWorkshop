import json

from flask import Flask, jsonify, request

app = Flask("WeatherAPI")


def get_temps():
    with open("temps.json", "r") as file:
        temps = file.read()
        temps = json.loads(temps)

    return temps


def save_temps(temps):
    with open("temps.json", "w") as file:
        temps = json.dumps(temps)
        file.write(temps)


def get_temp(city):
    temps = get_temps()
    temp = temps.get(city,-1)
    return temp


def add_temp(city, temp):
    temps = get_temps()
    temps[city] = temp
    save_temps(temps)


@app.route("/")
def index():
    return "Weather API is running :)"


@app.route("/get_temp")
def api_get_temp():
    city = request.args.get("city")
    temp = get_temp(city)
    return str(temp)


@app.route("/get_temps")
def api_get_temps():
    temps = get_temps()
    return jsonify(temps)


@app.route("/add_temp")
def api_add_temp():
    city = request.args.get("city")
    temp = request.args.get("temp", type=int)
    add_temp(city, temp)
    return "successfull update"


app.run(port=8000)
