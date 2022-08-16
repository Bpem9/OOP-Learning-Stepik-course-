class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    def __init__(self, *args):
        self.recipe = []
        if args is not None:
            for arg in args:
                self.recipe.append(arg)

    def add_ingredient(self, ing):
        self.recipe.append(ing)

    def remove_ingredient(self, ing):
        self.recipe.remove(ing)

    def get_ingredients(self):
        names = [str(ing) for ing in self.recipe]
        return tuple(names)

    def __len__(self):
        return len(self.recipe)
ing1 = Ingredient('Яйца', 3, 'шт')
rp = Recipe(ing1, Ingredient('Вода', 0.5, 'литра'))
ing2 = Ingredient('Мука', 15, 'грамм')
rp.add_ingredient(Ingredient('Соль', 2, 'грамма'))
rp.add_ingredient(ing2)
print(*rp.get_ingredients(), sep='\n')
rp.remove_ingredient(ing2)
print('===============================')
print(*rp.get_ingredients(), sep='\n')
print(ing2)
