# Import library
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
df = pd.read_csv(r"D:\SEMESTER 6\PRAK_MESIN\1227050026_Arief Rahman Mubarok_UTS_Prak_Pembelajaran_Mesin\1227050026_Arief Rahman Mubarok_Praktikum_Pembelajaran_Mesin\citrus.csv")  # Pastikan file citrus.csv ada di folder yang sama  # Pastikan file citrus.csv ada di folder yang sama

# Cek data awal
print(df.head())

# Pisahkan fitur dan label
X = df.drop("name", axis=1)
y = df["name"]

# Encode label (string ke angka)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Bagi data menjadi data latih dan uji
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Buat dan latih model Gaussian Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)

# Prediksi data uji
y_pred = model.predict(X_test)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=le.classes_)

# Cetak hasil evaluasi
print(f"\nAkurasi: {accuracy:.2f}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(report)
