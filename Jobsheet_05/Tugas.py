# Tugas.py
# -*- coding: utf-8 -*-
"""
Analisis sampling lengkap sesuai permintaan:
1) Simple Random Sampling (n=20)
2) Stratified Sampling (Region, 5 per region)
3) Systematic Sampling (step=5)
4) Cluster Sampling (pilih 2 region acak)
Analisis statistik (Age, Income), simulasi distribusi mean (1000 x n=30),
eksperimen ukuran sampel (n=10,50,100), plotting dan ringkasan.
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# ====== KONFIGURASI ======
# Otomatis mendeteksi path file di folder Downloads
downloads_path = os.path.expanduser("~/Downloads")
data_path = os.path.join(downloads_path, "sampling_dataset.csv")

print("Memeriksa path file:")
print(" ->", data_path)

if not os.path.exists(data_path):
    print("\n❌ File tidak ditemukan di lokasi tersebut.")
    print("Isi folder Downloads kamu:")
    print(os.listdir(downloads_path))
    raise FileNotFoundError(f"File tidak ditemukan: {data_path}")

# Random seed untuk reproduksibilitas
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# ====== BACA DATA ======
df = pd.read_csv(data_path)
print("\n✅ File ditemukan dan berhasil dibaca!")
print("Ukuran dataset:", df.shape)
print("Kolom:", df.columns.tolist())

# Pastikan kolom Age, Income, Region ada
for c in ["Age", "Income", "Region"]:
    if c not in df.columns:
        raise ValueError(f"Kolom '{c}' tidak ditemukan di dataset. Pastikan dataset memiliki kolom: Age, Income, Region")

# ====== FUNGSI SAMPLING ======
def simple_random_sampling(df, k, random_state=None):
    return df.sample(n=k, replace=False, random_state=random_state).reset_index(drop=True)

def stratified_sampling(df, strata_col, k_per_strata, random_state=None):
    rng = np.random.RandomState(random_state)
    groups = []
    for val, group in df.groupby(strata_col):
        n = min(len(group), k_per_strata)
        groups.append(group.sample(n=n, random_state=rng.randint(0, 10**9)))
    return pd.concat(groups).reset_index(drop=True)

def systematic_sampling(df, step, start=None):
    n = len(df)
    if start is None:
        start = 0
    idx = np.arange(start, n, step)
    return df.iloc[idx].reset_index(drop=True)

def cluster_sampling(df, cluster_col, n_clusters, random_state=None):
    rng = np.random.RandomState(random_state)
    clusters = df[cluster_col].dropna().unique()
    if len(clusters) < n_clusters:
        raise ValueError("Jumlah cluster unik kurang dari n_clusters yang diminta.")
    chosen = rng.choice(clusters, size=n_clusters, replace=False)
    sample = df[df[cluster_col].isin(chosen)].reset_index(drop=True)
    return sample, chosen

# ====== TERAPKAN SAMPLING ======
srs_sample = simple_random_sampling(df, 20, random_state=RANDOM_STATE)
strat_sample = stratified_sampling(df, "Region", 5, random_state=RANDOM_STATE)
systematic_sample = systematic_sampling(df, step=5, start=0)
cluster_sample, chosen_clusters = cluster_sampling(df, "Region", 2, random_state=RANDOM_STATE)

print("\nCluster terpilih:", chosen_clusters)
print("Ukuran sampel SRS:", len(srs_sample))
print("Ukuran sampel Stratified:", len(strat_sample))
print("Ukuran sampel Systematic:", len(systematic_sample))
print("Ukuran sampel Cluster:", len(cluster_sample))

# ====== STATISTIK SAMPEL ======
def sample_stats(sample, name):
    return {
        "name": name,
        "n": len(sample),
        "age_mean": sample["Age"].mean(),
        "age_std": sample["Age"].std(ddof=1),
        "income_mean": sample["Income"].mean(),
        "income_std": sample["Income"].std(ddof=1)
    }

stats_list = [
    sample_stats(srs_sample, "Simple Random (n=20)"),
    sample_stats(strat_sample, "Stratified (5 per region)"),
    sample_stats(systematic_sample, f"Systematic (step=5, n={len(systematic_sample)})"),
    sample_stats(cluster_sample, f"Cluster (clusters={list(chosen_clusters)})")
]
stats_df = pd.DataFrame(stats_list)
print("\nStatistik masing-masing sampel:")
print(stats_df.to_string(index=False))

# ====== PROPORSI REGION ======
pop_region = df["Region"].value_counts(normalize=True).sort_index()
def region_prop(sample):
    return sample["Region"].value_counts(normalize=True).reindex(pop_region.index).fillna(0)
compare = pd.DataFrame({
    "population": pop_region,
    "srs": region_prop(srs_sample),
    "strat": region_prop(strat_sample),
    "systematic": region_prop(systematic_sample),
    "cluster": region_prop(cluster_sample)
}).T
print("\nProporsi Region (populasi vs sampel):")
print(compare)

# ====== SIMULASI DISTRIBUSI RATA-RATA (1000x n=30) ======
def sampling_distribution_of_mean(df, col="Income", sample_size=30, n_sims=1000, random_state=None):
    rng = np.random.RandomState(random_state)
    n = len(df)
    means = []
    for _ in range(n_sims):
        idx = rng.choice(n, size=sample_size, replace=False)
        means.append(df.iloc[idx][col].mean())
    return np.array(means)

pop_income_mean = df["Income"].mean()
pop_income_std = df["Income"].std(ddof=0)
means_1000 = sampling_distribution_of_mean(df, col="Income", sample_size=30, n_sims=1000, random_state=RANDOM_STATE)

print(f"\nMean pendapatan populasi = {pop_income_mean:.3f}, std populasi = {pop_income_std:.3f}")
print(f"Mean dari distribusi sampling (n=30, 1000 sims): mean={means_1000.mean():.3f}, std={means_1000.std(ddof=1):.3f}")

# ====== PLOT HASIL ======
os.makedirs("outputs", exist_ok=True)
plt.figure(figsize=(8,5))
sns.histplot(means_1000, bins=30, kde=True)
plt.axvline(pop_income_mean, color="r", linestyle="--", label=f"Pop mean = {pop_income_mean:.2f}")
plt.title("Distribusi rata-rata Income (1000 sampel, n=30)")
plt.xlabel("Rata-rata Income per sampel")
plt.ylabel("Frekuensi")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/sampling_dist_n30.png", dpi=150)
print("📊 Histogram sampling (n=30) disimpan di: outputs/sampling_dist_n30.png")

skewness = stats.skew(means_1000)
kurt = stats.kurtosis(means_1000)
print(f"Skewness (means): {skewness:.4f}   Excess kurtosis: {kurt:.4f}")

# ====== EKSPERIMEN UKURAN SAMPEL (10, 50, 100) ======
def experiment_sample_sizes(df, sizes=[10,50,100], n_sims=1000, col="Income", random_state=None):
    rng = np.random.RandomState(random_state)
    n = len(df)
    results = {}
    for s in sizes:
        means = []
        for _ in range(n_sims):
            idx = rng.choice(n, size=s, replace=False)
            means.append(df.iloc[idx][col].mean())
        means = np.array(means)
        results[s] = {
            "means": means,
            "mean_of_means": means.mean(),
            "std_of_means": means.std(ddof=1)
        }
    return results

sizes = [10, 50, 100]
exp = experiment_sample_sizes(df, sizes=sizes, n_sims=1000, col="Income", random_state=RANDOM_STATE)

for s in sizes:
    m = exp[s]["mean_of_means"]
    sd = exp[s]["std_of_means"]
    print(f"\nUkuran sampel {s}: mean of means = {m:.3f}, std of means = {sd:.3f}")
    plt.figure(figsize=(7,4))
    sns.histplot(exp[s]["means"], bins=30, kde=True)
    plt.title(f"Distribusi rata-rata Income (n={s}, 1000 sims)")
    plt.xlabel("Rata-rata Income")
    plt.ylabel("Frekuensi")
    plt.tight_layout()
    plt.savefig(f"outputs/sampling_dist_n{s}.png", dpi=150)
    print(f"📈 Saved: outputs/sampling_dist_n{s}.png")

# Simpan ringkasan statistik
summary = pd.DataFrame([
    {"sample_size": s,
     "mean_of_means": exp[s]["mean_of_means"],
     "std_of_means": exp[s]["std_of_means"]}
    for s in sizes
])
summary.to_csv("outputs/summary_sample_sizes.csv", index=False)
print("💾 Ringkasan disimpan: outputs/summary_sample_sizes.csv")

# ====== KESIMPULAN ======
print("\n=== Kesimpulan singkat otomatis ===")
print("- Stratified sampling memberikan distribusi Region paling mirip populasi.")
print("- Cluster sampling efisien tapi bisa bias jika klaster tidak representatif.")
print("- Simple random cocok untuk populasi homogen.")
print("- Systematic mudah diterapkan; hati-hati jika data punya pola periodik.")
print("\nDistribusi mean sampel (n=30) mendekati normal (cek skewness & kurtosis).")
print("Semakin besar ukuran sampel, variasi mean semakin kecil (sesuai teori CLT).")
print("\n✅ Selesai! Periksa folder 'outputs' untuk grafik dan ringkasan CSV.")
