def calculate_risk_score(heart_rate, temperature):
    score = 0
    if heart_rate > 100:
        score += 1
    if temperature > 38.3 or temperature < 36:
        score += 1
    return score

def test_high_risk():
    assert calculate_risk_score(110, 39.0) == 2

def test_low_risk():
    assert calculate_risk_score(70, 37.0) == 0

def test_boundary():
    assert calculate_risk_score(101, 37.0) == 1
