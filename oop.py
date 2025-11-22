# Encapsulation inheritance polymorphsim Abstraction DRY


class Character:
    _power = 100
    _defence = 100
    _attack = 100

    __lives = 3

    def __init__(self, name):
        if name is None:
            self.name = "anonymous"
        else:
            self.name = name

    def move(self):
        print(f"{self.name} is moving")

    def attack(self):
        print(f"{self.name} is attacking")

    @property
    def power(self):
        return self._power


class Fly:
    def can_fly(self):
        print("I can fly")


class Robot(Character, Fly):
    battery = 100

    def __init__(self, name):
        super().__init__("robot " + name)
        self._power = 50

    def attack(self):
        print("robot attacking starts")
        super().attack()
        print("robot attacking ends")


class Giant_Robot(Robot):
    def __init__(self):
        super().__init__("Giant")
        self._power = 200

    def attack(self):
        print("Giant robot attacking with massive force!")
        super().attack()

class Animal_Robot(Robot):
    def __init__(self):
        super().__init__('Animal bot')


class Human(Character):
    hungary = 100

    def __init__(self, name):
        super().__init__("human " + name)
        self._power = 90
        
    def attack(self):
        print("human attacking starts")
        super()
        print("human attacking ends")



cat_bot = Animal_Robot()
giant_bot = Giant_Robot()

print(giant_bot.name)
giant_bot.can_fly()

wall_e = Robot("wall-e")
mustafa = Human("mustafa")


wall_e.move()
wall_e.can_fly()
mustafa.move()

wall_e.attack()
mustafa.attack()


print(wall_e.power)
print(mustafa.power)
print(wall_e.name)
print(mustafa.name)
