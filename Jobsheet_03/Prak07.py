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

    # =========================
    # Cek Missing Values
    # =========================
    missing_values = data.isnull().sum().sort_values(ascending=False)
    print("--- Missing Values per Column ---")
    print(missing_values, "\n")

    # Visualisasi missing values sebelum imputasi
    plt.figure(figsize=(12,6))
    sns.heatmap(data.isnull(), cbar=False, cmap="YlOrRd")
    plt.title("Missing Values Heatmap - Before Imputation")
    plt.show()

    # =========================
    # Imputasi Missing Values
    # =========================
    for column in data.columns:
        if data[column].isnull().any():
            if pd.api.types.is_numeric_dtype(data[column]):
                mean_val = data[column].mean()
                data[column] = data[column].fillna(mean_val)
                print(f"Imputed missing values in '{column}' with mean: {mean_val}")
            elif pd.api.types.is_object_dtype(data[column]):
                mode_val = data[column].mode()[0]
                data[column] = data[column].fillna(mode_val)
                print(f"Imputed missing values in '{column}' with mode: '{mode_val}'")
            else:
                print(f"Column '{column}' has unhandled dtype: {data[column].dtype}")

    # =========================
    # Cek Missing Values Setelah Imputasi
    # =========================
    missing_after = data.isnull().sum()
    print("\n--- Missing Values After Imputation ---")
    print(missing_after, "\n")

    # Visualisasi missing values setelah imputasi
    plt.figure(figsize=(12,6))
    sns.heatmap(data.isnull(), cbar=False, cmap="YlGnBu")
    plt.title("Missing Values Heatmap - After Imputation")
    plt.show()

except FileNotFoundError:
    print("❌ File tidak ditemukan. Pastikan path file sudah benar.")
except Exception as e:
    print(f"⚠️ Terjadi error: {e}")
