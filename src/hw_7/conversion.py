def inchs_to_centimeters(n: 'expected types int, float') -> float:
    """Return argument n as a representation in centimeters"""
    return round(n * 2.54, 2)


def centimeters_to_inchs(n: 'expected types int, float') -> float:
    """Returns argument n as a representation in Imperial inchs"""
    return round(n / 2.54, 2)


def miles_to_km(n: 'expected types int, float') -> float:
    """Returns argument n as a representation in kilometers"""
    return round(n * 1.609, 2)


def km_to_miles(n: 'expected types int, float') -> float:
    """Returns argument n as a representation in standard land miles"""
    return round(n / 1.609, 2)


def pounds_to_kilos(n: 'expected types int, float') -> float:
    """Returns argument n as a representation in kilograms"""
    return round(n * 0.453592, 2)


def kilos_to_pounds(n: 'expected types int, float') -> float:
    """Returns argument n as a representation in English pounds"""
    return round(n / 0.453592, 2)


def ounces_to_grams(n: 'expected types int, float') -> float:
    """Returns argument n as a representation in grams"""
    return round(n * 28.3495, 3)


def grams_to_ounces(n: 'expected types int, float') -> float:
    """Returns argument n as a representation in troy ounces"""
    return n / 28.3495


def gallons_to_liters(n: 'expected types int, float') -> float:
    """Returns argument n as a representation in liters"""
    return round(n * 3.78541, 2)


def liters_to_gallons(n: 'expected types int, float') -> float:
    """Returns argument n as a representation in American gallons"""
    return round(n / 3.8541, 2)


def pints_to_liters(n: 'expected types int, float') -> float:
    """Returns argument n as a representation in liters"""
    return round(n * 0.658261, 2)


def liters_to_pints(n: 'expected types int, float') -> float:
    """Returns argument n as a representation in English pints"""
    return round(n / 0.658261, 2)



