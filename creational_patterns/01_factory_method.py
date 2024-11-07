class Product:
    """
    Базовый класс отвечающий за продукт
    """
    def release(self):
        pass


class Car(Product):
    """
    Класс отвечающий за создание легковых машин
    """
    def release(self):
        print("Car is released")


class Truck(Product):
    """
    Класс отвечающий за создание грузовиков
    """
    def release(self):
        print("Truck is released")


class Factory:
    """
    Базовый класс для фабрик, декларирующий фабричный метод
    """
    def create(self) -> Product:
        pass


class CarFactory(Factory):
    """
    Класс фабрики отвечающей за создание легковых машин
    """
    def create(self) -> Product:
        return Car()


class TruckFactory(Factory):
    """
    Класс фабрики отвечающей за создание грузовиков
    """
    def create(self) -> Product:
        return Truck()


if __name__ == '__main__':
    creator = CarFactory()
    car = creator.create()

    creator = TruckFactory()
    truck = creator.create()

    car.release()
    truck.release()