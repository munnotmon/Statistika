# Import library yang dibutuhkan
import pandas as pd
import statistics

# Tentukan path file CSV yang mau dibuka
file_path = '/Users/ashadinoor/Downloads/Ecommerce_Consumer_Behavior_Analysis_Data.csv'

try:
    # Baca file CSV (gunakan sep otomatis)
    data = pd.read_csv(file_path, sep=None, engine='python')
    print("✅ File berhasil dibaca!\n")

    # Tampilkan 5 baris pertama
    print("=== 5 Baris Pertama Data ===")
    print(data.head(), "\n")

    # Bersihkan dan ubah kolom yang bisa jadi numerik
    for col in data.columns:
        # Hapus simbol non-numerik (misal $, %, ,)
        data[col] = (
            data[col]
            .astype(str)
            .str.replace('[^0-9.-]', '', regex=True)
        )
        # Coba ubah ke numerik kalau bisa
        try:
            data[col] = pd.to_numeric(data[col])
        except:
            pass

    # Tampilkan tipe data tiap kolom
    print("=== Tipe Data Tiap Kolom ===")
    print(data.dtypes, "\n")

    # Analisis Mean, Median, Mode untuk kolom numerik
    for column in data.select_dtypes(include=['number']):
        if data[column].notnull().any():
            mean_val = round(data[column].mean(), 2)
            median_val = round(data[column].median(), 2)
            try:
                mode_val = statistics.mode(data[column])
            except statistics.StatisticsError:
                mode_val = "No unique mode"

            print(f"--- Analysis for column '{column}' ---")
            print(f"Mean: {mean_val}")
            print(f"Median: {median_val}")
            print(f"Mode: {mode_val}\n")

except FileNotFoundError:
    print("❌ File tidak ditemukan. Pastikan path file sudah benar.")
except Exception as e:
    print(f"⚠️ Terjadi error: {e}")
