import pickle
import streamlit as st

# membaca model
diabetes_model_svm = pickle.load(open("diabetes_model_svm.sav", "rb"))
diabetes_model_rf = pickle.load(open("diabetes_model_rf.sav", "rb"))

# judul web
st.title("Website Prediksi Diabetes")

model = st.selectbox(label="Pilih Model", options=("SVM", "Random Forest"))

# membagi kolom
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.text_input("Input nilai pregnancies")
    bloodPressure = st.text_input("Input nilai blood pressure")
    insulin = st.text_input("Input nilai insulin")
    diabetesPredigreeFunction = st.text_input("Input nilai diabetes predigree function")

with col2:
    glucose = st.text_input("Input nilai glucose")
    skinThickness = st.text_input("Input nilai skin thickness")
    bmi = st.text_input("Input nilai bmi")
    age = st.text_input("Input nilai age")

# code utk prediksi
diabetes_diagnosis = ""

# membuat tombol utk prediksi
if st.button("Tes Prediksi Diabetes"):
    if "SVM" in model:
        diabetes_prediction = diabetes_model_svm.predict(
            [
                [
                    pregnancies,
                    glucose,
                    bloodPressure,
                    skinThickness,
                    insulin,
                    bmi,
                    diabetesPredigreeFunction,
                    age,
                ]
            ]
        )

    if "Random Forest" in model:
        diabetes_prediction = diabetes_model_rf.predict(
            [
                [
                    pregnancies,
                    glucose,
                    bloodPressure,
                    skinThickness,
                    insulin,
                    bmi,
                    diabetesPredigreeFunction,
                    age,
                ]
            ]
        )

    if diabetes_prediction[0] == 1:
        diabetes_diagnosis = "Pasien terkena diabetes"
    else:
        diabetes_diagnosis = "Pasien tidak terkena diabetes"

    st.success(diabetes_diagnosis)
