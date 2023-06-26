import json
from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf8') as file:
    cook_book = {}
    for dish_name in file:
        ing_count = int(file.readline())
        ing_list = []
        for i in range(ing_count):
            n, q, m = file.readline().strip().split('|')
            ing_list.append({
                'ingredient_name': n, 'quantity': q, 'measure': m
                })
        file.readline()
        cook_book[dish_name.strip()] = ing_list
    res = json.dumps(cook_book, ensure_ascii=False, indent=2)


def get_shop_list_by_dishes(dishes, person_count):
    list_ = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            if ing['ingredient_name'] not in list_.keys():
                measure = ing['measure']
                quantity = int(ing['quantity']) * person_count
                list_[ing['ingredient_name']] = {
                    'quantity': quantity, 'measure': measure
                    }
            elif ing['ingredient_name'] in list_.keys():
                measure = ing['measure']
                quantity = int(ing['quantity']) * person_count + \
                    int((list_[ing['ingredient_name']])['quantity'])
                list_[ing['ingredient_name']] = {
                    'quantity': quantity, 'measure': measure
                    }

    return list_


pprint(get_shop_list_by_dishes(['Утка по-пекински', 'Запеченный картофель'], 2))