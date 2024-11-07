from abc import ABCMeta, abstractmethod


class Body(metaclass=ABCMeta):
    @abstractmethod
    def release_body(self):
        pass


class FenderBody(Body):
    def release_body(self):
        print("stratocaster body")


class GibsonBody(Body):
    def release_body(self):
        print("les paul body")


class Guitar(metaclass=ABCMeta):
    @abstractmethod
    def release_guitar(self, body: Body):
        pass


class FenderGuitar(Guitar):
    def release_guitar(self, body: Body):
        print("Fender released guitar with:", end=' ')
        body.release_body()


class GibsonGuitar(Guitar):
    def release_guitar(self, body: Body):
        print("Gibson released guitar with:", end=' ')
        body.release_body()


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def create_body(self) -> Body:
        pass

    @abstractmethod
    def create_guitar(self) -> Guitar:
        pass


class FenderFactory(Factory):
    def create_body(self) -> Body:
        return FenderBody()

    def create_guitar(self) -> Guitar:
        return FenderGuitar()


class GibsonFactory(Factory):
    def create_body(self) -> Body:
        return GibsonBody()

    def create_guitar(self) -> Guitar:
        return GibsonGuitar()


if __name__ == '__main__':
    fender = FenderFactory()
    f_body = FenderBody()
    f_guitar = FenderGuitar()

    f_guitar.release_guitar(f_body)

    gibson = GibsonFactory()
    g_body = GibsonBody()
    g_guitar = GibsonGuitar()

    g_guitar.release_guitar(g_body)
