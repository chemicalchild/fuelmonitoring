from flask import request, render_template, url_for, jsonify
from fuelmonitoring import app, db
from fuelmonitoring.Model import LocationFuelData

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('About.html')


@app.route('/receive_data', methods=['POST'])
def receive_data():
    try:
        data = request.json

        location_fuel_data = LocationFuelData(
            latitude =data.get('Latitude'),
            longitude =data.get('Longitude'),
            altitude =data.get('Altitude'),
            fuel_level = data.get('TannkLevel')
        )
        db.session.add(location_fuel_data)
        db.session.commit()
        return "Data received sucessfully", 200
    except Exception as e:
        return str(e), 400



#This route sends the data to the front end
@app.route('/send_data', methods=['GET'])
def get_data():
    try:
        data = LocationFuelData.query.all()
        data_list = []

        for item in data:
            data_entry = {
                'latitude': item.latitude,
                'longitude': item.longitude,
                'altitude': item.altitude,
                'fuel_level': item.fuel_level,
                'timestamp': item.timestamp
            }
            data_list.append(data_entry)
            print(data_entry)
        return jsonify(data_list), 200
    except Exception as e:
        return str(e), 400

