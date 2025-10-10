# Import library yang dibutuhkan
import pandas as pd
import statistics

# Tentukan path file CSV
file_path = '/Users/ashadinoor/Downloads/Ecommerce_Consumer_Behavior_Analysis_Data.csv'

try:
    # Baca file CSV
    data = pd.read_csv(file_path, sep=None, engine='python')
    print("✅ File berhasil dibaca!\n")

    # Tampilkan 5 baris pertama
    print("=== 5 Baris Pertama Data ===")
    print(data.head(), "\n")

    # Tampilkan tipe data tiap kolom
    print("=== Tipe Data Tiap Kolom ===")
    print(data.dtypes, "\n")

    # Analisis kolom numerik
    for column in data.select_dtypes(include=['int64', 'float64']):
        if data[column].notnull().any():
            mean_val = round(data[column].mean(), 2)
            median_val = round(data[column].median(), 2)
            try:
                mode_val = statistics.mode(data[column])
            except statistics.StatisticsError:
                mode_val = "No unique mode"

            variance_val = round(data[column].var(), 2)
            std_dev_val = round(data[column].std(), 2)

            print(f"--- Analysis for column '{column}' ---")
            print(f"Mean              : {mean_val} (Rata-rata)")
            print(f"Median            : {median_val} (Nilai tengah)")
            print(f"Mode              : {mode_val} (Nilai yang paling sering muncul)")
            print(f"Variance          : {variance_val} (Sebaran data)")
            print(f"Standard Deviation: {std_dev_val} (Akar kuadrat variance)\n")
        else:
            print(f"--- Analysis for column '{column}' ---")
            print("Kolom hanya berisi null values. Tidak bisa dihitung statistik.\n")

except FileNotFoundError:
    print("❌ File tidak ditemukan. Pastikan path file sudah benar.")
except Exception as e:
    print(f"⚠️ Terjadi error: {e}")
