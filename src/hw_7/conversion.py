from typing import Union


def inchs_to_centimeters(inchs: Union[int, float]) -> float:
    """Returns inchs as a representation in centimeters"""
    return round(inchs * 2.54, 2)


def centimeters_to_inchs(centimeters: Union[int, float]) -> float:
    """Returns centimeters as a representation in Imperial inchs"""
    return round(centimeters / 2.54, 2)


def miles_to_km(miles: Union[int, float]) -> float:
    """Returns miles as a representation in kilometers"""
    return round(miles * 1.609, 2)


def km_to_miles(km: Union[int, float]) -> float:
    """Returns kilometers as a representation in standard land miles"""
    return round(km / 1.609, 2)


def pounds_to_kilos(n: Union[int, float]) -> float:
    """Returns pounds as a representation in kilograms"""
    return round(n * 0.453592, 2)


def kilos_to_pounds(n: Union[int, float]) -> float:
    """Returns kilograms as a representation in English pounds"""
    return round(n / 0.453592, 2)


def ounces_to_grams(n: Union[int, float]) -> float:
    """Returns ounces as a representation in grams"""
    return round(n * 28.3495, 3)


def grams_to_ounces(n: Union[int, float]) -> float:
    """Returns grams as a representation in troy ounces"""
    return n / 28.3495


def gallons_to_liters(n: Union[int, float]) -> float:
    """Returns gallons as a representation in liters"""
    return round(n * 3.78541, 2)


def liters_to_gallons(n: Union[int, float]) -> float:
    """Returns liters as a representation in American gallons"""
    return round(n / 3.8541, 2)


def pints_to_liters(n: Union[int, float]) -> float:
    """Returns pints as a representation in liters"""
    return round(n * 0.658261, 2)


def liters_to_pints(n: Union[int, float]) -> float:
    """Returns liters as a representation in English pints"""
    return round(n / 0.658261, 2)
