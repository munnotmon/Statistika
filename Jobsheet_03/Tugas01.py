# Import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tentukan path file CSV
file_path = '/Users/ashadinoor/Downloads/Titanic-Dataset.csv'

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
    # 1. Cek Missing Values di 'Age' dan 'Fare'
    # =========================
    for col in ['Age', 'Fare']:
        missing_count = data[col].isnull().sum()
        print(f"Kolom '{col}' memiliki {missing_count} missing values.")

    # =========================
    # 2. Cek distribusi data
    # =========================
    plt.figure(figsize=(12,5))

    plt.subplot(1,2,1)
    sns.histplot(data['Age'], kde=True, bins=30, color='skyblue')
    plt.title("Distribusi 'Age'")

    plt.subplot(1,2,2)
    sns.histplot(data['Fare'], kde=True, bins=30, color='salmon')
    plt.title("Distribusi 'Fare'")

    plt.tight_layout()
    plt.show()

    # =========================
    # 3. Simple Imputation
    # =========================
    # Untuk 'Age' (numerik, biasanya gunakan median karena ada outlier)
    age_median = data['Age'].median()
    data['Age'] = data['Age'].fillna(age_median)
    print(f"\nMissing values di 'Age' diimputasi dengan median: {age_median}")

    # Untuk 'Fare' (numerik, bisa pakai mean)
    fare_mean = data['Fare'].mean()
    data['Fare'] = data['Fare'].fillna(fare_mean)
    print(f"Missing values di 'Fare' diimputasi dengan mean: {fare_mean:.2f}")

    # Verifikasi setelah imputasi
    print("\n--- Missing Values Setelah Imputasi ---")
    print(data[['Age', 'Fare']].isnull().sum())

except FileNotFoundError:
    print("❌ File tidak ditemukan. Pastikan path file sudah benar.")
except Exception as e:
    print(f"⚠️ Terjadi error: {e}")
