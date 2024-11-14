from copy import deepcopy


class Sheep:
    __name: str = ''
    __params: dict = {'Weight': 20, 'Height': .34}

    def __init__(self, donor: "Sheep" = None):
        if donor is not None:
            self.__name = donor.get_name()
            self.__params = deepcopy(donor.get_params())


    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def get_params(self) -> dict:
        return self.__params

    def set_weight(self, weight: int):
        self.__params['Weight'] = weight

    def clone(self):
        return Sheep(self)


if __name__ == '__main__':
    sheep_donor: Sheep = Sheep()
    sheep_donor.set_name('Dolly')

    sheep_clone: Sheep = sheep_donor.clone()

    print('Donor is: ', sheep_donor.get_name(), sheep_donor.get_params())
    print('Clone is: ', sheep_clone.get_name(), sheep_clone.get_params())

    sheep_clone.set_name('New Dolly')
    sheep_clone.set_weight(25)

    print('Donor is: ', sheep_donor.get_name(), sheep_donor.get_params())
    print('Clone is: ', sheep_clone.get_name(), sheep_clone.get_params())