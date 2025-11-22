# Encapsulation inheritance polymorphsim Abstraction


# class Vehicle:
#     length = 100
#     _engine_weight = 1000

#     def __init__(self, weight):
#         if weight < 0:
#             raise ValueError("Weight cannot be negative")
#         self.weight = weight

#     def __repr__(self):
#         return "length: " + str(self.length) + " weight: " + str(self.weight)

#     def _calculate_sum(self):
#         return self.weight + self._engine_weight


class Robot:
    color = "red"
    _power = 100
    _defence = 100
    _attack = 100

    __point = 0

    def __init__(self, name):
        self.name = name

    def reset_point(self):
        if self._power > 1000:
            print("are you sure?")
        else:
            self.__point = 0
            
    def add_point(self, value):
        self.__point += value

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, value):
        if value < 0:
            raise ValueError("Point cannot be negative")
        if value > 10000:
            raise ValueError("Point cannot be larger than 10000")
        self.__point = value



robot_one = Robot("mustafa")
robot_two = Robot("ahmet")

robot_one.point = -5


print(robot_one.name)
print(robot_two.reset_point())
