import math
from datetime import datetime
import time


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


def log(func):
    def wrapper(*args, **kwargs):
        print("calculation begins")
        print(datetime.now().timestamp())
        time.sleep(1)
        result = func(*args, **kwargs)
        print("calculation ends")
        print(datetime.now().timestamp())
        return result

    return wrapper


@repeat(3)
@log
def selam():
    print("Hello")


selam()


@log
def calculate_sum(a, b):
    return a + b


print(calculate_sum(1, 2))


class Vector:
    PI = 3.14123213131231

    def __init__(self, x_init=0, y_init=0, x_end=0, y_end=0):
        if x_init == x_end and y_init == y_end:
            raise ValueError
        self.x_init = x_init
        self.y_init = y_init
        self.x_end = x_end
        self.y_end = y_end
        self._created_at = datetime.now()
        self.__delete_time = datetime.now()

    @property
    def created_at(self):
        # format unix time to datetime
        return self._created_at.strftime("%Y-%m-%d %H:%M:%S")

    @created_at.setter
    def created_at(self, value: datetime):
        if value < self._created_at:
            raise ValueError
        self._created_at = value

    @log
    def get_length(self):
        return math.sqrt(
            (self.x_end - self.x_init) ** 2 + (self.y_end - self.y_init) ** 2
        )

    @staticmethod
    def get_sum(a, b):
        return a + b

    @classmethod
    def get_vectors(cls, *args):
        return [cls(*arg) for arg in args]

    def __add__(self, other):
        new_x_init = self.x_init + other.x_init
        new_y_init = self.y_init + other.y_init
        new_x_end = self.x_end + other.x_end
        new_y_end = self.y_end + other.y_end

        return Vector(new_x_init, new_y_init, new_x_end, new_y_end)

    def __lt__(self, next_vector):
        return self.get_length() < next_vector.get_length()

    def __len__(self):
        return int(self.get_length())


vector_one = Vector(1, 1, 2, 2)
vector_two = Vector(2, 2, 3, 3)

vector_three = vector_two + vector_one + vector_one

vector_one.get_length()

# print(vector_three.x_init, vector_three.y_init, vector_three.x_end, vector_three.y_end)

# print(vector_one < vector_two)

# length_one = len(vector_one)

# print(length_one)


# vectors = Vector.get_vectors((1, 1, 2, 2), (2, 2, 3, 3), (3, 3, 4, 4))
# sum = math.pi


# print(vector_one.created_at)

# vector_one.created_at = datetime(2025, 11, 10)

# print(vector_one._created_at)
