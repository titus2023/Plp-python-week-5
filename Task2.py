class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement this method.")

    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method.")

    def eat(self):
        raise NotImplementedError("Subclass must implement this method.")

  class Dog(Animal):
    def move(self):
        return "The dog runs on four legs."

    def make_sound(self):
        return "The dog barks: Woof! Woof!"

    def eat(self):
        return "The dog eats meat and bones."

class Bird(Animal):
    def move(self):
        return "The bird flies in the sky."

    def make_sound(self):
        return "The bird chirps: Tweet! Tweet!"

    def eat(self):
        return "The bird eats seeds and insects."

class Fish(Animal):
    def move(self):
        return "The fish swims in the water."

    def make_sound(self):
        return "The fish is silent... glub glub."

    def eat(self):
        return "The fish eats algae and smaller fish."

class Snake(Animal):
    def move(self):
        return "The snake slithers on the ground."

    def make_sound(self):
        return "The snake hisses: Sssss!"

    def eat(self):
        return "The snake eats eggs, rodents, and frogs."

  def animal_call_them(animal):
    print(animal.move())
    print(animal.make_sound())
    print(animal.eat())
    print("-" * 40) #decoration

# Create animal objects
animals = [Dog(), Bird(), Fish(), Snake()]

# Show behavior for each animal
for a in animals:
    animal_call_them(a)
