    # Import library
import os
import pandas as pd
import pickle
import numpy as np
from flask import Flask, redirect, render_template, url_for, request, json
# from app import main

# Create flask app
app = Flask(__name__)

# app.config
rbf_model = pickle.load(open('linear_model.pkl', 'rb'))

# Render landing page
@app.route('/')
def index():
    return render_template('index.html')

# Render predict page
@app.route('/predict')
def predictt():
    return render_template('klasifikasi.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil nilai input dari form dan konversi ke tipe float

    Age = request.form['Age']
    
    Gender = request.form['Gender']
    if not (1 <= int(Gender) <= 2):
        return 'Smoking harus berada antara 1 dan 2'
    Dust_Allergy = request.form['Dust Allergy']
    if not (1 <= int(Dust_Allergy) <= 10):
        return 'Dust Allergy harus berada antara 1 dan 10'
    Smoking= request.form['Smoking']
    if not (1 <= int(Smoking) <= 10):
        return 'Smoking harus berada antara 1 dan 10'
    Balance_Diet= request.form['Balance Diet']
    if not (1 <= int(Balance_Diet) <= 7):
        return 'Balance Diet harus berada antara 1 dan 7'
    Fatigue= request.form['Fatigue']
    if not (1 <= int(Fatigue) <= 10):
        return 'Fatigue harus berada antara 1 dan 10'
    Snoring= request.form['Snoring']
    if not (1 <= int(Snoring) <= 7):
        return 'Snoring harus berada antara 1 dan 7'
    Frequent_Cold = request.form['Frequent Cold']
    if not (1 <= int(Frequent_Cold) <= 10):
        return 'Frequent Cold harus berada antara 1 dan 10'
    Air_Pollution = request.form['Air Pollution']
    if not (1 <= int(Air_Pollution) <= 10):
        return 'Air Pollution harus berada antara 1 dan 10'
    Genetic_Risk = request.form['Genetic Risk']
    if not (1 <= int(Genetic_Risk) <= 10):
        return 'Genetic Risk harus berada antara 1 dan 10'
    Chronic_Lung_Disease = request.form['Chronic Lung Disease']
    if not (1 <= int(Chronic_Lung_Disease) <= 7):
        return 'Chronic Lung Disease harus berada antara 1 dan 7'
    Chest_Pain= request.form['Chest Pain']
    if not (1 <= int(Chest_Pain) <= 9):
        return 'Chest Pain harus berada antara 1 dan 9'
    Wheezing= request.form['Wheezing']
    if not (1 <= int(Wheezing) <= 10):
        return 'Wheezing harus berada antara 1 dan 10'
    Clubbing_of_Finger_Nails= request.form['Clubbing of Finger Nails']
    if not (1 <= int(Clubbing_of_Finger_Nails) <= 10):
        return 'Clubbing of Finger Nails harus berada antara 1 dan 10'
    Dry_Cough = request.form['Dry Cough']
    if not (1 <= int(Dry_Cough) <= 10):
        return 'Dry Cough Nails harus berada antara 1 dan 10'

    input_data = [Age,
    Gender,                       
    Air_Pollution,                
    Dust_Allergy,
    Chronic_Lung_Disease,
    Genetic_Risk,             
    Smoking,                
    Chest_Pain,            
    Balance_Diet,
    Fatigue,              
    Wheezing,                
    Snoring,     
    Clubbing_of_Finger_Nails,    
    Frequent_Cold,      
    Dry_Cough]
    print(input_data)
    input_data = np.array(input_data).reshape(1, -1)
    
    # Lakukan prediksi dengan model
    prediction = rbf_model.predict(input_data)[0]
    if prediction == 0:
        result = 'Beresiko Rendah Terkena Kanker Paru'
    elif prediction == 1:
        result = 'Beresiko Sedang Terkena Kanker Paru'
    else:
        result = 'Beresiko Tinggi Terkena Kanker Paru'
    return render_template('klasifikasi.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)

# Render predict page
# @app.route('/result', methods=['POST'])
# def result_predict():
#     if request.method == 'POST':
#         volatile_acidity = float(request.form['VolatileAcidity'])
#         citric_acid = float(request.form['CitricAcid'])
#         chlorides = float(request.form['Chlorides'])
#         total_sulfur_dioxide = float(request.form['TotalSulfurDioxide'])
#         sulphates = float(request.form['Sulphates'])
#         alcohol = float(request.form['Alcohol'])
        
        # input_data = (volatile_acidity, citric_acid, chlorides,
        # total_sulfur_dioxide, sulphates, alcohol)

#         input_data_as_np_array = np.asarray(input_data)
#         input_data_reshaphed = input_data_as_np_array.reshape(1,-1)
#         prediction = rf_model.predict(input_data_reshaphed)

#         if (prediction[0] == 1):
#             result = 'Good Quality'
#             url = "https://em-content.zobj.net/source/microsoft-teams/337/winking-face_1f609.png"
#         else:
#             result = 'Sorry, your wine is Bad Quality'
#             url = "https://em-content.zobj.net/source/microsoft-teams/337/worried-face_1f61f.png"

#         return render_template('result.html', result=result, url_img=url)
#     else:
#         return redirect(url_for('predict'))