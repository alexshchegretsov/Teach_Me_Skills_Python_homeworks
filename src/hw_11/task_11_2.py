"""
Создать класс Car.
Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
Методы: увеличить скорости(скорость + 5),
уменьшение скорости(скорость  - 5),
стоп(сброс скорости на 0),
отображение скорости,
разворот(изменение знака скорости).
Все атрибуты приватные.

"""


class Car:
    """
    A class to use to represent a car

    Attributes
    ----------
    brand : str
        represent a car brand
    model : int, str
        the car model
    year_issue : int
        the year of car manufacture
    speed : int
        the car speed (default 0)

    Methods
    ----------
    speed_up
        Increases speed by 5
    speed_down
        Decreases speed by 5
    stop
        Resets speed to zero
    turn
        Represents speed change

    """

    def __init__(self, brand, model, year_issue, speed=0):
        """
        The constructor for Car class.

        Parameters
        ----------
        brand : str
            The car brand.
        model : str, int
            The car model.
        year_issue : int
            The year of car manufacture.
        speed : int
            The car speed, optional
        """
        self.__brand = brand
        self.__model = model
        self.__year_issue = year_issue
        self.__speed = speed

    def speed_up(self):
        """Increases speed by 5"""
        self.__speed += 5

    def speed_down(self):
        """Decreases speed by 5"""
        self.__speed -= 5

    def stop(self):
        """Resets speed to zero"""
        self.__speed *= 0

    @property
    def speed(self):
        """Returns speed value"""
        return self.__speed

    # Is it turn?
    @speed.setter
    def speed(self, value):
        """Sets speed"""
        self.__speed = value


car_1 = Car('zhiguli', '2101', 1990)

car_1.speed_up()
print(car_1.speed)
car_1.stop()
car_1.speed = 20
print(car_1.speed)