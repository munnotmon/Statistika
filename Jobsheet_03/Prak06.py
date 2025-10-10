# Import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tentukan path file CSV
file_path = '/Users/ashadinoor/Downloads/Ecommerce_Consumer_Behavior_Analysis_Data.csv'

try:
    # Baca file CSV
    data = pd.read_csv(file_path)
    print("✅ File berhasil dibaca!\n")

    # Tampilkan 5 baris pertama
    print("=== 5 Baris Pertama Data ===")
    print(data.head(), "\n")

    # Tampilkan tipe data tiap kolom
    print("=== Tipe Data Tiap Kolom ===")
    print(data.dtypes, "\n")

    # Cek missing values per kolom
    missing_values = data.isnull().sum().sort_values(ascending=False)
    print("--- Missing Values per Column ---")
    print(missing_values, "\n")

    # Cek apakah ada missing values di seluruh DataFrame
    if missing_values.sum() > 0:
        print("⚠️ The DataFrame contains missing values.")
    else:
        print("✅ The DataFrame does not contain any missing values.")

except FileNotFoundError:
    print("❌ File tidak ditemukan. Pastikan path file sudah benar.")
except Exception as e:
    print(f"⚠️ Terjadi error: {e}")
