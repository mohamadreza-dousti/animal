from Animals.animal import Animal
import pygame

class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        self.wing_span = wing_span
        super().__init__(name, species, age, sound)


    def _AddAnimal__add_animal(self):
        Animal.animals.append({"Zoo":Animal.zoo_name, "Name":self.name,
                               "Species":self.species, "Age":self.age,
                               "Sound":"voice", "Wing span":self.wing_span})

    def make_sound(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

    def info(self):
        return (f"name:{self.name}\nspecies:{self.species}\n"
                f"age:{self.age}\nsound:voice")