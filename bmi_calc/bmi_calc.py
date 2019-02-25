def calc(weight, cm):
    height = (cm/100) ** 2
    return round((weight/height), 2)
