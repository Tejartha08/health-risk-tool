from flask import Flask, render_template, request
from risk_calculators import DiabetesRiskCalculator, HeartDiseaseRiskCalculator, ObesityRiskCalculator
from recommendations import generate_recommendations

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/assess', methods=['POST'])
def assess():
    data = {
        'age': int(request.form['age']),
        'sex': request.form['sex'],
        'bmi': float(request.form['bmi']),
        'systolic_bp': int(request.form['systolic_bp']),
        'diastolic_bp': int(request.form['diastolic_bp']),
        'smoking': request.form.get('smoking') == 'yes',
        'family_diabetes': request.form.get('family_diabetes') == 'yes',
        'family_heart': request.form.get('family_heart') == 'yes',
        'physical_activity': request.form['physical_activity'],
        'diet_quality': request.form['diet_quality']
    }

    diabetes_risk = DiabetesRiskCalculator.calculate(data)
    heart_risk = HeartDiseaseRiskCalculator.calculate(data)
    obesity_risk = ObesityRiskCalculator.calculate(data)

    recommendations = generate_recommendations(diabetes_risk, heart_risk, obesity_risk, data)

    return render_template("results.html", 
                           diabetes_risk=diabetes_risk, 
                           heart_risk=heart_risk, 
                           obesity_risk=obesity_risk, 
                           recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
