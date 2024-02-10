import numpy as np
import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import path

dir = path.Path(__file__).abspath()
sys.append.path(dir.parent.parent)


def diabetes_prediction(input_data):
    df = pd.read_csv('diabetes.csv')
    scaler = StandardScaler()
    scaler.fit_transform(df.drop(columns='Outcome', axis=1))

    loaded_model = pickle.load(open('trained_model.sav', 'rb'))

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    std_data = scaler.transform(input_data_reshaped)

    prediction = loaded_model.predict(std_data)
    if not prediction[0]:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
def show_diabetes_analysis():  
    st.header("Machine Learning Model Used for Training")
    st.write("Model: Support Vector Machine")
    st.write("Accuracy score for the training data:  0.7866449511400652")
    st.write("Accuracy score for the test data:  0.7727272727272727")

    diabetes_data = pd.read_csv("diabetes.csv")
    st.header("Data Exploration and Analysis")
    correlation = pd.DataFrame(diabetes_data).corr()
   
    # Plot the heatmap
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size': 8}, cmap='Blues', ax=ax)
    plt.title("Correlation Heatmap")

    st.pyplot(fig)

    st.subheader(f"Data Size: {diabetes_data.shape}")
    st.subheader("First 5 rows of the diabetes dataset")
    st.dataframe(diabetes_data.head())

    st.subheader("Statistical measures of the diabetes dataset")
    st.dataframe(diabetes_data.describe())

def show_diabetes_prediction_system():
    st.title("Diabetes Prediction System 🩸🔮")

    show_analysis = st.checkbox("About Data and Trained Machine Learning Model")
    if show_analysis:
        show_diabetes_analysis()
    else:
        st.image("diabetes_prediction.gif", use_column_width=True)
        st.header("Input Fields for Personalized Diabetes Prognosis")

        # Getting input data from the user
        Pregnancies = st.text_input("Number of Pregnancies")
        Glucose = st.text_input("Glucose Level")
        BloodPressure = st.text_input("Blood Pressure Value")
        SkinThickness = st.text_input("Skin Thickness Value")
        Insulin = st.text_input("Insulin Level")
        BMI = st.text_input("BMI Value")
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
        Age = st.text_input("Age of the Person")

        diagnosis = ''

        if st.button("Predict Diabetes", disabled=not Pregnancies or not Glucose or not BloodPressure or not SkinThickness or not Insulin or not BMI or not DiabetesPedigreeFunction or not Age):
            diagnosis = diabetes_prediction((int(Pregnancies), int(Glucose), int(BloodPressure), int(SkinThickness), int(Insulin), float(BMI), float(DiabetesPedigreeFunction), int(Age)))
        if diagnosis != '':
            st.success(diagnosis)

def heart_disease_analysis():  
    st.header("Machine Learning Model Used for Training")
    st.write("Model: Logistic Regression")
    st.write("Accuracy score for the training data:  0.8512396694214877")
    st.write("Accuracy score for the test data:  0.819672131147541")

    st.header("Data Exploration and Analysis")

    heart_disease_df = pd.read_csv("heart_disease_data.csv")
    st.subheader(f"Data Size: {heart_disease_df.shape}")
    st.subheader("First 5 rows of the diabetes dataset")
    st.dataframe(heart_disease_df.head())

    st.subheader("Statistical measures of the diabetes dataset")
    st.dataframe(heart_disease_df.describe())

    st.subheader("Visualization")
    fig, ax = plt.subplots(figsize=(30, 15))
    sns.barplot(x='age', y='target', data=heart_disease_df, ax=ax)
    plt.title("Heart Disease Probabilty by Age")
    plt.xlabel("Age")
    plt.ylabel("Heart Disease Probabilty")

    st.pyplot(fig)

def heart_disease_prediction(input_data):
    loaded_model = pickle.load(open('heart_disease_trained_model.sav', 'rb'))

    input_data_as_numpy_array= np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if not prediction[0]:
        return 'The Person does not have a Heart Disease'
    else:
        return 'The Person has Heart Disease'

def show_heart_disease_prediction_system():
    st.title("Heart Disease Prediction System 🩺💓")

    show_analysis = st.checkbox("About Data and Trained Machine Learning Model")
    if show_analysis:
        heart_disease_analysis()
    else:
        st.image("heart_disease.gif", use_column_width=True)
        st.header("Input Fields for Personalized Heart Disease Prognosis")

        # Getting input data from the user
        age = st.text_input("Age of the Person")
        sex = st.number_input("Sex of the Person", min_value=0, max_value=1, step=1)
        cp = st.number_input("Chest Pain Type", min_value=0, max_value=3, step=1)
        trestbps = st.text_input("Resting Blood Pressure")
        chol = st.text_input("Serum Cholestoral in mg/dl")
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")
        restecg = st.number_input("Resting Electrocardiographic Results", min_value=0, max_value=2, step=1)
        thalach = st.text_input("Maximum Heart Rate Achieved")
        exang = st.text_input("Exercise induced Angina")
        oldpeak = st.text_input("Oldpeak = ST depression induced by exercise relative to rest")
        slope = st.text_input("The slope of the peak exercise ST segment")
        ca = st.number_input("Number of major vessels (0-3) colored by flourosopy", min_value=0, max_value=3, step=1)
        thal = st.number_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect", min_value=0, max_value=3, step=1)
        
        diagnosis = ''

        if st.button("Predict Heart Disease"):
            diagnosis = heart_disease_prediction((int(age),int(sex),int(cp),int(trestbps),int(chol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),float(slope),int(ca),int(thal)))
        if diagnosis != '':
            st.success(diagnosis)

def main():
    predictive_systems = ["Select a System", "Diabetes Prediction System", "Heart Disease Prediction System"]

    st.sidebar.title("Select Predictive System")
    selected_system = st.sidebar.selectbox("", predictive_systems, index=0)

    # Display information about the selected predictive system
    if selected_system != "Select a System":
        if selected_system == "Diabetes Prediction System":
            show_diabetes_prediction_system()
        elif selected_system == "Heart Disease Prediction System":
            show_heart_disease_prediction_system()
    else:
        st.title("Predictive Wonders: A Glimpse into Machine Learning Mastery 🚀✨")
        st.image("Machine-Learning.gif", use_column_width=True)

    


if __name__ == "__main__":
    main()