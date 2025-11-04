from Animals import animal, bird

if __name__ == "__main__":
    parrot = bird.Bird("parrot", "Rose-ringed", 2, "sound.mp3", 12)
    lion = animal.Animal("lion", "large cat", 23, "ROAR!")
    print(f"count of animals(lion class):{lion.get_count()}")
    print(f"count of animals(bird class):{parrot.get_count()}")
    print(f"parrot info\n{parrot.info()}")
    print(f"lion info\n{lion.info()}")
    parrot.make_sound()
    print(f"animals: {parrot.get_animals()}")