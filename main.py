
from enum import Enum, auto
import random


class Taste(Enum):
    SWEET = auto()
    SOUR = auto()
    NEUTRAL = auto()


class Fruit:
    def __init__(self, name, size, color, taste, cost):
        self.name = name
        self.size = size
        self.color = color
        self.taste = taste
        self.cost = cost

    def __repr__(self):
        return f"{self.name} ({self.size}, {self.color}, {self.taste.name}, ${self.cost})"


class Topping(Enum):
    CHOCOLATE = (Taste.SWEET,)
    LEMON = (Taste.SOUR,)
    YOGURT = (Taste.NEUTRAL,)

    def __init__(self, taste):
        self.taste = taste


class FruitSalad:
    def __init__(self, fruits, topping=None):
        self.fruits = fruits
        self.topping = topping

    def choose_topping(self):
        tastes = [fruit.taste for fruit in self.fruits]
        if all(taste == Taste.SWEET for taste in tastes):
            self.topping = Topping.CHOCOLATE
        elif all(taste == Taste.SOUR for taste in tastes):
            self.topping = Topping.LEMON
        else:
            self.topping = Topping.YOGURT

    def mix_ingredients(self):
        random.shuffle(self.fruits)

    def total_cost(self):
        return sum(fruit.cost for fruit in self.fruits)

    def __repr__(self):
        return f"FruitSalad({self.fruits}, Topping: {self.topping.name if self.topping else 'None'}, Total Cost: ${self.total_cost()})"


class Recipe:
    def __init__(self, salad, fixed_cost):
        self.salad = salad
        self.fixed_cost = fixed_cost

    def total_cost(self):
        return self.salad.total_cost() + self.fixed_cost

    def __repr__(self):
        return f"Recipe({self.salad}, Fixed Cost: ${self.fixed_cost}, Total Cost: ${self.total_cost()})"


fruits1 = [
    Fruit("Apple", "Medium", "Red", Taste.SWEET, 1.5),
    Fruit("Banana", "Large", "Yellow", Taste.SWEET, 1.0),
    Fruit("Strawberry", "Small", "Red", Taste.SWEET, 0.8)
]

fruits2 = [
    Fruit("Lemon", "Small", "Yellow", Taste.SOUR, 0.5),
    Fruit("Lime", "Small", "Green", Taste.SOUR, 0.4),
    Fruit("Orange", "Medium", "Orange", Taste.SWEET, 0.7)
]


salad1 = FruitSalad(fruits1)
salad2 = FruitSalad(fruits2)


salad1.choose_topping()
salad2.choose_topping()


recipe1 = Recipe(salad1, fixed_cost=2.0)
recipe2 = Recipe(salad2, fixed_cost=1.5)


recipes = [recipe1, recipe2]


def find_cheapest_recipe(recipes):
    cheapest_recipe = recipes[0]
    for recipe in recipes[1:]:
        if recipe.total_cost() < cheapest_recipe.total_cost():
            cheapest_recipe = recipe
    return cheapest_recipe


best_recipe = find_cheapest_recipe(recipes)


print("Recipes:")
for recipe in recipes:
    print(recipe)

print("\nMost cost-effective recipe:")
print(best_recipe)
