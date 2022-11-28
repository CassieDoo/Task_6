from pprint import pprint
cook_book = {}
with open('1recipes.txt', 'r', encoding='utf-8') as recipes:
    while True:
        compound = []
        ingredients = []
        details = ['ingredient_name', 'quantity', 'measure']
        name_dish = recipes.readline().rstrip()
        quantity_of_ingredients = recipes.readline().rstrip()
        if quantity_of_ingredients.isdigit():
            for line in range(int(quantity_of_ingredients)):
                ingredients.append(recipes.readline().rstrip())
            for ingredient in ingredients:
                details_of_ingredient = ingredient.split(' | ')
                explanation_of_ingredients = dict(zip(details, details_of_ingredient))
                compound.append(explanation_of_ingredients)
            recipes.readline().rstrip()
            cook_book[name_dish] = compound
        else:
            break
pprint(cook_book)
