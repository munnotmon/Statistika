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

    # --- Histograms ---
    for col in data.select_dtypes(include=['int64', 'float64']):
        if data[col].notnull().any():
            plt.figure(figsize=(8, 6))
            sns.histplot(data[col], kde=True)
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()

    # --- Box plots ---
    for col in data.select_dtypes(include=['int64', 'float64']):
        if data[col].notnull().any():
            plt.figure(figsize=(8, 6))
            sns.boxplot(y=data[col])
            plt.title(f'Box Plot of {col}')
            plt.ylabel(col)
            plt.show()

    # --- Scatter plot (contoh: Purchase Amount vs Age) ---
    if 'Purchase Amount (USD)' in data.columns and 'Age' in data.columns:
        if data['Purchase Amount (USD)'].notnull().any() and data['Age'].notnull().any():
            plt.figure(figsize=(8, 6))
            sns.scatterplot(x='Age', y='Purchase Amount (USD)', data=data)
            plt.title('Scatter Plot of Purchase Amount vs. Age')
            plt.xlabel('Age')
            plt.ylabel('Purchase Amount (USD)')
            plt.show()

    # --- Bar plot (contoh: Gender) ---
    if 'Gender' in data.columns:
        if data['Gender'].notnull().any():
            plt.figure(figsize=(8, 6))
            sns.countplot(x='Gender', data=data)
            plt.title('Distribution of Gender')
            plt.xlabel('Gender')
            plt.ylabel('Count')
            plt.show()

except FileNotFoundError:
    print(f"Error: The file '{file_path}' tidak ditemukan.")
except Exception as e:
    print(f"Terjadi error: {e}")
