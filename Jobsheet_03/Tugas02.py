# Import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

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
    # 1. Imputasi missing values 'Age' dengan mean
    # =========================
    age_mean = data['Age'].mean()
    data['Age'].fillna(age_mean, inplace=True)
    print(f"Missing values di 'Age' diimputasi dengan mean: {age_mean:.2f}\n")

    # =========================
    # 2. Hitung z-score untuk 'Age'
    # =========================
    data['Age_zscore'] = (data['Age'] - data['Age'].mean()) / data['Age'].std()
    print("=== 5 Baris Pertama Z-Score 'Age' ===")
    print(data[['Age', 'Age_zscore']].head(), "\n")

    # =========================
    # 3. Tentukan jumlah outlier |Z| > 3
    # =========================
    outliers = data[data['Age_zscore'].abs() > 3]
    outliers_count = outliers.shape[0]
    print(f"Jumlah outlier pada 'Age' (|Z| > 3): {outliers_count}\n")

    # =========================
    # 4. Peluang Age < 20 (asumsi normal)
    # =========================
    mean_age = data['Age'].mean()
    std_age = data['Age'].std()
    prob_age_less_20 = stats.norm.cdf(20, loc=mean_age, scale=std_age)
    print(f"Peluang 'Age' < 20 (asumsi normal): {prob_age_less_20:.4f}\n")

    # =========================
    # 5. Visualisasi distribusi 'Age' dengan highlight outlier
    # =========================
    plt.figure(figsize=(10,6))
    
    # Semua data
    sns.histplot(data['Age'], kde=True, color='skyblue', bins=30, label='Age')
    
    # Outlier
    sns.histplot(outliers['Age'], kde=False, color='red', bins=30, label='Outlier (|Z|>3)')
    
    plt.title("Distribusi 'Age' dengan Highlight Outlier")
    plt.axvline(20, color='green', linestyle='--', label='Age = 20')
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

except FileNotFoundError:
    print("❌ File tidak ditemukan. Pastikan path file sudah benar.")
except Exception as e:
    print(f"⚠️ Terjadi error: {e}")
