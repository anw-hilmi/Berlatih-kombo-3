import joblib
import glob
import os

# Sesuaikan path-nya, jika model.pkl ada di folder yang sama dengan app.py, gunakan './*.pkl'
list_of_files = glob.glob('./*.pkl') 

if not list_of_files:
    raise FileNotFoundError("Tidak ada file .pkl yang ditemukan. Pastikan modelling.py sudah dijalankan.")

latest_file = max(list_of_files, key=os.path.getctime)
model = joblib.load(latest_file)