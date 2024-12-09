class Animal:
    alive = []

    def __init__(
            self, name:
            str, health: int = 100,
            hidden: bool = False
    ) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}"
                f"}}")

    @classmethod
    def update_alive(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

    @classmethod
    def __str__(cls) -> str:
        return "[" + ", ".join(repr(animal) for animal in cls.alive) + "]"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(beast: Animal) -> None:
        if isinstance(beast, Herbivore) and not beast.hidden:
            beast.health -= 50
            if beast.health <= 0:
                beast.health = 0
                Animal.update_alive()
