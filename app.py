from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS  

app = Flask(__name__)

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
        print(f"Lokasi diterima: {latitude}, {longitude}")
        return jsonify({"status": "sukses", "message": "Lokasi diterima"}), 200
    else:
        return jsonify({"status": "gagal", "message": "Data tidak lengkap"}), 400

@app.route('/')
def index():
    return "Server aktif dan siap menerima lokasi."

if __name__ == '__main__':
    app.run(debug=True)
