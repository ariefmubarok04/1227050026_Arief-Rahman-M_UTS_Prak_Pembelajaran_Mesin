# 1227050026_Arief-Rahman-M_UTS_Prak_Pembelajaran_Mesin
# UTS Praktikum Pembelajaran Mesin  
## Naive Bayes – Klasifikasi Citrus (Jeruk vs Anggur)

### 👤 Nama: Arief Rahman Mubarok  
### 🆔 NIM: 1227050026  

---

## 📌 Deskripsi
Project ini bertujuan untuk membangun model klasifikasi buah (jeruk atau anggur) menggunakan algoritma **Naive Bayes** berdasarkan data fitur ukuran dan warna buah. Dataset yang digunakan berupa `citrus.csv`.

---

## 🔧 Tools & Library
- Python 3.x
- Pandas
- scikit-learn

---

## 🧪 Tahapan & Langkah-Langkah

### 1. **Import Library**
Import pustaka yang dibutuhkan seperti `pandas`, `sklearn`, dan `os`.

### 2. **Load Dataset**
Gunakan `pandas.read_csv()` untuk membaca file `citrus.csv`.

### 3. **Eksplorasi Data**
Lihat beberapa data awal dan informasi dataset:
- Kolom: `diameter`, `weight`, `red`, `green`, `blue`, `name`
- Label (`name`) berisi: `orange`, `grapefruit`

### 4. **Preprocessing**
- Pisahkan fitur (`X`) dan label (`y`)
- Encode label string menjadi numerik (menggunakan `LabelEncoder`)
- Split data menjadi data latih dan uji (`train_test_split`)

### 5. **Pembuatan Model**
- Gunakan `GaussianNB` dari `sklearn.naive_bayes`
- Latih model menggunakan `fit()`

### 6. **Evaluasi Model**
- Lakukan prediksi pada data uji
- Hitung:
  - **Accuracy**
  - **Confusion Matrix**
  - **Classification Report** (precision, recall, f1-score)

---

## 📈 Hasil Evaluasi
Contoh hasil:
- Akurasi: 92%
- Confusion Matrix menunjukkan prediksi yang cukup seimbang antara kedua kelas

---

## 📂 Struktur Folder

