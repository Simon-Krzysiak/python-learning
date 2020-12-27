"""Task:
    You are given a list dishes, where each element consists of a list of
    strings beginning with the name of the dish, followed by all the
    ingredients used in preparing it. You want to group the dishes by
    ingredients, so that for each ingredient you'll be able to find all the
    dishes that contain it (if there are at least 2 such dishes).

    Return an array where each element is a list beginning with the
    ingredient name, followed by the names of all the dishes that contain
    this ingredient. The dishes inside each list should be sorted
    lexicographically, and the result array should be sorted
    lexicographically by the names of the ingredients.
"""


def groupingDishes(dishes):
    dishes_with = dict()

    for dish in dishes:
        for ingredient in dish[1:]:
            dishes_with.setdefault(ingredient, []).append(dish[0])

    ingredients = list()
    for ingredient in dishes_with:
        if len(dishes_with[ingredient]) >= 2:
            dishes_with[ingredient].sort()
            ingredients.append([ingredient] + dishes_with[ingredient])

    return sorted(ingredients)
