def calculate_score(plastic, transport, diet, energy):
    score = 100
    tips = []

    score -= plastic * 2
    if plastic > 5:
        tips.append("Switch to reusable alternatives to cut plastic waste.")

    if transport == "Car":
        score -= 25
        tips.append("Public transport or cycling reduces emissions significantly.")
    elif transport == "Public Transport":
        score -= 10

    if diet == "Meat-heavy":
        score -= 20
        tips.append("Reducing meat consumption lowers your carbon footprint.")
    elif diet == "Mixed":
        score -= 10

    if energy > 8:
        score -= 15
        tips.append("Turn off unused appliances to save electricity.")

    return max(score, 0), tips
