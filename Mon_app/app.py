from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("random_forest_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    balance = float(request.form['balance'])
    num_products = int(request.form['num_products'])
    is_active = int(request.form['is_active'])

    # Sexe
    gender = request.form['gender']
    if gender == 'Female':
        gender_female = 1 
    else : gender_female=0
    if gender == 'Male':
        gender_male = 1 
    else : gender_male=0

    # Geographie
    geo = request.form['geography']
    if geo == 'France' :
        geo_france = 1 
    else :geo_france= 0
    if geo == 'Germany' :
        geo_germany = 1 
    else :geo_germany= 0
    if geo == 'Spain':
        geo_spain = 1 
    else :geo_spain = 0

    features = np.array([[age, balance, num_products, is_active,
                        geo_france, geo_germany, geo_spain,
                        gender_female, gender_male]])

    prediction = model.predict(features)
    return render_template('index.html', Prediction=f"Résultat : {int(prediction)}")


if __name__ == '__main__':
    app.run(debug=True)