# risk_calculators.py

class DiabetesRiskCalculator:
    @staticmethod
    def calculate(data):
        score = 0
        if data['age'] > 45:
            score += 0.3
        if data['bmi'] >= 30:
            score += 0.4
        elif data['bmi'] >= 25:
            score += 0.2
        if data['family_diabetes']:
            score += 0.2
        if data['physical_activity'] == 'low':
            score += 0.2
        if data['diet_quality'] == 'poor':
            score += 0.2
        return min(score, 1.0)

class HeartDiseaseRiskCalculator:
    @staticmethod
    def calculate(data):
        score = 0
        if (data['sex'] == 'M' and data['age'] > 50) or (data['sex'] == 'F' and data['age'] > 55):
            score += 0.3
        if data['systolic_bp'] >= 140 or data['diastolic_bp'] >= 90:
            score += 0.3
        if data['smoking']:
            score += 0.3
        if data['family_heart']:
            score += 0.2
        if data['physical_activity'] == 'low':
            score += 0.2
        return min(score, 1.0)

class ObesityRiskCalculator:
    @staticmethod
    def calculate(data):
        score = 0
        if data['bmi'] >= 30:
            score += 0.7
        elif data['bmi'] >= 25:
            score += 0.4
        if data['physical_activity'] == 'low':
            score += 0.3
        if data['diet_quality'] == 'poor':
            score += 0.3
        return min(score, 1.0)
