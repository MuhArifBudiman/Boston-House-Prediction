# 🏡 Boston House Price Prediction  
📌 Machine Learning Regression using XGBoost + Business Insights

---

## 📖 Overview

Proyek ini bertujuan untuk memprediksi harga rumah di Boston menggunakan algoritma **Machine Learning Regression**.  
Selain prediksi, proyek ini juga menyediakan **insights bisnis** terhadap fitur apa saja yang paling memengaruhi nilai properti, sehingga dapat membantu stakeholder seperti:

- Developer properti
- Tim marketing
- Konsultan real estate  
- Data-driven policy maker

Insight ini dapat digunakan sebagai dasar strategi penjualan, segmentasi market, dan pengembangan unit perumahan.

---

## 🎯 Problem Statement

Bagaimana cara memprediksi harga rumah di Boston secara akurat berdasarkan atribut lingkungan dan demografi, serta mengetahui variabel mana yang berkontribusi paling besar terhadap nilai properti?

---

## 📊 Dataset Summary

- Total: **506 rows**
- Features: **13 independent variables**
- Target: **MEDV (Median House Value)**

### Data Cleaning & Preprocessing

| Task | Method |
|------|--------|
| Missing values | Median imputation |
| Outliers | Winsorization using IQR |
| Scaling | StandardScaler |
| Train/Test Split | 80/20 |

---

## 🧠 Model Experiments

Beberapa model dicoba untuk baseline:

- Random Forest Regressor
- Gradient Boosting
- **XGBoost (Selected Model)** ✔️

### ⚙️ Selected Model Performance — **XGBoost**

| Stage | Train Accuracy | Test Accuracy | R² Score |
|-------|----------------|---------------|----------|
| Before Tuned | 0.999 | 0.898 | 0.898 |
| **After Hyperparameter Tuning** | **0.97** | **0.90** | **0.8182** |

📌 *Hyperparameter tuning membantu mengurangi overfitting dan meningkatkan generalisasi.*

---

## 🔍 Feature Importance

Model menunjukkan fitur yang paling berpengaruh terhadap harga rumah:

| Rank | Feature | Insight |
|------|---------|--------|
| 1 | RM | Semakin banyak kamar → harga meningkat |
| 2 | LSTAT | Semakin tinggi populasi berpenghasilan rendah → harga turun |
| 3 | PTRATIO | Semakin ideal rasio guru-murid → harga naik |
| 4 | TAX | Pajak properti memengaruhi nilai |
| 5 | CRIM | Area dengan kriminalitas lebih tinggi → harga lebih rendah |

📈 Visualisasi feature importance tersedia pada folder `visualization`.

---

## 🚀 How to Run

### 1️⃣ Clone Repository
```sh
git clone https://github.com/username/boston-house-price-prediction.git
cd boston-house-price-prediction

```

🧾 Business Value Summary

Model ini memberikan:

- ✔️ Prediksi harga properti secara akurat
- ✔️ Identifikasi faktor penting untuk strategi marketing dan development
- ✔️ Pendekatan explainable ML melalui feature importance
- ✔️ Reproducible workflow untuk deployment dan experimentation


-- NOTE: Untuk detail project ini ada pada file pdf sebagai gambaran besar project berlangsung dan hasil EDA di dalam folder notebook

- Muhammad Arif Budiman
- 0877 8862 0153
