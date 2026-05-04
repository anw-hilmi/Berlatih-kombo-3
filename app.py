import joblib
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # ... kode prediksi Anda ...
    return jsonify({"status": "success"})

# LETAKKAN DI SINI (Paling Bawah)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)