import pandas as pd
import numpy as np

# Membuat dataset contoh
np.random.seed(42) # Untuk reproduksibilitas
n = 100
data = {
    'Provinsi': np.random.choice(['Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'DKI Jakarta'], size=n),
    'Usia': np.random.randint(18, 65, size=n),
    'Pendapatan': np.random.randint(5000000, 50000000, size=n),
    'Pendidikan': np.random.choice(['SMA', 'D1', 'D3', 'S1', 'S2', 'S3'], size=n)
}
df = pd.DataFrame(data)

# 1. Simple Random Sampling (Pengambilan sampel acak sederhana)
# Mengambil 20 sampel secara acak dari seluruh populasi
n_samples = 20
simple_random_sample = df.sample(n=n_samples, random_state=42) # random_state untuk reproduksibilitas

print("Simple Random Sample:")
print(simple_random_sample)
print("\nPenjelasan: Setiap individu dalam populasi memiliki peluang yang sama untuk terpilih dalam sampel.")

# 2. Systematic Sampling (Pengambilan sampel sistematis)
# Mengambil sampel setiap k individu dalam populasi
k = 5 # Interval sampling
systematic_sample = df.iloc[::k]

print("\nSystematic Sample:")
print(systematic_sample)
print("\nPenjelasan: Mengambil sampel pada interval tertentu. Misalnya, setiap ke-5 individu.")

# 3. Stratified Sampling (Pengambilan sampel berlapis)
# Membagi populasi berdasarkan provinsi dan mengambil sampel dari setiap strata
strata = df.groupby('Provinsi')
stratified_sample = strata.apply(lambda x: x.sample(n=int(n_samples/len(strata)), random_state=42))
# jumlah sampel proporsional untuk setiap strata

print("\nStratified Sample:")
print(stratified_sample)
print("\nPenjelasan: Populasi dibagi menjadi beberapa kelompok (strata), kemudian diambil sampel dari setiap strata.")

# 4. Cluster Sampling (Pengambilan sampel kluster)
# 💡 Membagi populasi menjadi kluster,
# kemudian memilih beberapa kluster secara acak dan mengambil semua individu di dalam kluster tersebut.

# Misal kita bagi berdasarkan provinsi sebagai kluster, dan mengambil 2 provinsi
clusters = df['Provinsi'].unique()
selected_clusters = np.random.choice(clusters, size=2, replace=False) # Mengambil 2 provinsi secara random

cluster_sample = df[df['Provinsi'].isin(selected_clusters)]

print("\nCluster Sample:")
print(cluster_sample)
print("\nPenjelasan: Populasi dibagi menjadi kelompok-kelompok (kluster), lalu beberapa kluster dipilih secara acak. ")

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 1. Populasi dan Sampel

# Misalnya, kita punya populasi tinggi badan mahasiswa.
populasi_tinggi_badan = np.random.normal(loc=165, scale=10, size=1000) # 1000 data, rata-rata 165 cm, standar deviasi 10 cm

# Mengambil sampel acak berukuran 30 dari populasi
ukuran_sampel = 30
sampel_tinggi_badan = np.random.choice(populasi_tinggi_badan, size=ukuran_sampel, replace=False)