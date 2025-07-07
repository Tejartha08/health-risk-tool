# recommendations.py

def generate_recommendations(diabetes, heart, obesity, data):
    recs = []

    if diabetes > 0.5:
        recs.append((1, "Improve diet: Increase fiber and reduce sugar intake"))
        recs.append((2, "Increase physical activity: Aim for at least 150 mins/week"))
        if data['bmi'] >= 25:
            recs.append((3, "Work on reducing BMI below 25 with professional guidance"))

    if heart > 0.5:
        recs.append((1, "Quit smoking to lower heart disease risk"))
        recs.append((2, "Control blood pressure: Monitor regularly and limit salt intake"))
        recs.append((3, "Adopt a heart-healthy diet rich in fruits, vegetables, and whole grains"))

    if obesity > 0.5:
        recs.append((1, "Focus on weight management through balanced meals"))
        recs.append((2, "Increase daily physical activity, even simple walking"))
        recs.append((3, "Consider a healthcare provider’s advice for a long-term plan"))

    if diabetes <= 0.5 and heart <= 0.5 and obesity <= 0.5:
        recs.append((1, "Maintain your current healthy lifestyle to keep your risks low"))

    recs.sort(key=lambda x: x[0])
    return recs
