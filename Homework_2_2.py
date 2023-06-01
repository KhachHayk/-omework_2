

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for name_dishes in file:
        number_ingredients = int(file.readline())
        ingredients = []
        for i in range(number_ingredients):
            name_ingredient, amount, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': name_ingredient,
                'quantity': amount,
                'measure': measure
            })
        file.readline()
        cook_book[name_dishes.strip()] = ingredients

def get_shop_list_by_dishes(name_dishes, person_count):
    shop_list = {}
    for dish in name_dishes:
        for ing in cook_book[dish]:
            i = {ing['ingredient_name']: {'measure': ing['measure'], 'quantity': ing['quantity'] * person_count}}
    shop_list.dict.update(i)
    return shop_list

