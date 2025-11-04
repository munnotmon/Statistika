import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 1. Populasi dan Sampel

# Misalnya, kita punya populasi tinggi badan mahasiswa.
populasi_tinggi_badan = np.random.normal(loc=165, scale=10, size=1000) # 1000 data, rata-rata 165 cm, standar deviasi 10 cm

# Mengambil sampel acak berukuran 30 dari populasi
ukuran_sampel = 30
sampel_tinggi_badan = np.random.choice(populasi_tinggi_badan, size=ukuran_sampel, replace=False)

# 2. Menghitung Distribusi Sampling Rata-Rata Sampel

# Simulasi pengambilan banyak sampel (misalnya, 1000 sampel)
banyak_sampel = 1000
rata_rata_sampel = []

for _ in range(banyak_sampel):
    sampel = np.random.choice(populasi_tinggi_badan, size=ukuran_sampel, replace=False)
    rata_rata_sampel.append(np.mean(sampel))

rata_rata_sampel = np.array(rata_rata_sampel)

# 3. Visualisasi Distribusi Sampling

plt.figure(figsize=(10, 6))
plt.hist(rata_rata_sampel, bins=30, density=True, alpha=0.7, label='Distribusi Sampling')

# Menambahkan garis vertikal untuk rata-rata populasi
plt.axvline(np.mean(populasi_tinggi_badan), color='red', linestyle='dashed', linewidth=2, label='Rata-rata Populasi')

# Menambahkan kurva distribusi normal untuk membandingkan
rata_rata_distribusi_sampling = np.mean(rata_rata_sampel)
standar_deviasi_distribusi_sampling = np.std(rata_rata_sampel)
x = np.linspace(min(rata_rata_sampel), max(rata_rata_sampel), 100)
plt.plot(x, stats.norm.pdf(x, loc=rata_rata_distribusi_sampling, scale=standar_deviasi_distribusi_sampling),
         'b-', lw=2, label='Distribusi Normal')

plt.xlabel('Rata-rata Tinggi Badan (cm)')
plt.ylabel('Frekuensi')
plt.title('Distribusi Sampling Rata-rata Tinggi Badan')
plt.legend()
plt.show()