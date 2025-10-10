# Import library yang dibutuhkan
import pandas as pd

# Tentukan path file CSV yang mau dibuka
file_path = '/Users/ashadinoor/Downloads/Ecommerce_Consumer_Behavior_Analysis_Data.csv'

# Buka file CSV pakai pandas
try:
    # Baca file CSV ke dalam DataFrame
    data = pd.read_csv(file_path)

    # Tampilkan 5 baris pertama untuk cek
    print(data.head())

except FileNotFoundError:
    print("❌ File tidak ditemukan. Pastikan path file sudah benar.")
except Exception as e:
    print("⚠️ Terjadi error:", e)
