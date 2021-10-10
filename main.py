import random
import string

letters = string.ascii_letters


class Car(object):
    def __init__(self, name: str, vin_number: str, model: str):
        self.name = name
        self.vin_number = vin_number
        self.model = model

    def __str__(self):
        return "Car(name=" + self.name + ', vin_number=' + self.vin_number + ", model=" + self.model + ")"

    def __repr__(self):
        return self.name


class Human(object):
    def __init__(self, name: str, age: int, current_car: Car, cars: list):
        self.cars = cars
        self.current_car = current_car
        self.age = age
        self.name = name

    def __str__(self):
        return f"Его зовут {self.name} - {self.age} возраст, он катается на {self.current_car}, Гараж из {len(self.cars)} машин(ы) "


garage1 = []
garage2 = []
quantiny1 = random.randint(1, 8)
quantiny2 = 9 - quantiny1
for j in range(quantiny1):
    garage1.append(Car(name=''.join(random.choice(letters) for names in range(10)),
                       vin_number=''.join(random.choice(letters) for numbers in range(5)),
                       model=''.join(random.choice(letters) for models in range(10))))
for j in range(quantiny2):
    garage2.append(Car(name=''.join(random.choice(letters) for names in range(10)),
                       vin_number=''.join(random.choice(letters) for numbers in range(5)),
                       model=''.join(random.choice(letters) for models in range(10))))

human1 = Human(name="Valera", age=54, current_car=garage1[random.randrange(quantiny1)], cars=garage1)
human2 = Human(name="Denis", age=27, current_car=garage2[random.randrange(quantiny2)], cars=garage2)

choice = input(f"1 - {human1.name} , 2 - {human2.name} выберите номер - ")

match int(choice):
    case 1:
        choiceCar = input(f"на какой машинке поедет {human1.name} выберите по номеру от 0 до {quantiny1} - ")
        human1.current_car = garage1[int(choiceCar)]
        print(f'{human1.name} поедет на машине {human1.current_car}')
    case 2:
        choiceCar = input(f"на какой машинке поедет {human2.name} выберите по номеру от 0 до {quantiny2} - ")
        human2.current_car = garage2[int(choiceCar)]
        print(f'{human2.name} поедет на машине {human2.current_car}')
