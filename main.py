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

    @classmethod
    def create_random(cls):
        return cls(
            name="".join(random.choice(letters) for _ in range(10)),
            vin_number="".join(random.choice(letters) for _ in range(5)),
            model="".join(random.choice(letters) for _ in range(10)),
        )


class Human(object):
    def __init__(self, name: str, age: int, current_car: Car, cars: list):
        self.cars = cars
        self.current_car = current_car
        self.age = age
        self.name = name

    def __str__(self):
        return f"Его зовут {self.name} - {self.age} возраст, он катается на {self.current_car}, Гараж из {len(self.cars)} машин(ы) "

    @classmethod
    def create_human(cls, name: str, age: int):
        garage = [Car.create_random() for _ in range(random.randint(1, 9))]
        return Human(name=name, age=age, current_car=random.choice(garage), cars=garage)


def main() -> None:
    try:
        human1 = Human.create_human("Valera", 54)
        human2 = Human.create_human("Denis", 27)
        choice = input(f"1 - {human1.name} , 2 - {human2.name} выберите номер - ")
        while True:
            match int(choice):


                case 1:
                    choiceCar = input(
                        f"на какой машинке поедет {human1.name} выберите по номеру от 0 до {len(human1.cars)} - ")
                    human1f.current_car = human1.cars[int(choiceCar) - 1]
                    print(f'{human1.name} поедет на машине {human1.current_car}')
                    break
                case 2:
                    choiceCar = input(
                        f"на какой машинке поедет {human2.name} выберите по номеру от 0 до {len(human2.cars)} - ")
                    human2.current_car = human2.cars[int(choiceCar) - 1]
                    print(f'{human2.name} поедет на машине {human2.current_car}')
                    break
                case _:
                    print("Ошибка нету такого ")
                    break

    except ValueError:
        print("Вы ввели не число")


if __name__ == "__main__":
    main()
