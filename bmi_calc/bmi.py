# Bmi Calc


def bmicalc(kg, cm):
    metre = (cm / 100) ** 2
    return round((kg / metre), 1)
