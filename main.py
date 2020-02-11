def parse_ingredient(ingredient: str):
    try:
        ingredient_name, quantity, measure = ingredient.split('|')
        return {
            'ingredient_name': ingredient_name.strip(),
            'quantity': int(quantity.strip()),
            'measure': measure.strip()
        }
    except ValueError:
        print('В файле ошибка')


def get_cook_book_from_file():
    cook_book = {}
    with open('recipes.txt') as file:
        while file.readline():
            dishes_name = file.readline().strip()
            ingredient_count = int(file.readline())
            ingredient_list = [parse_ingredient(file.readline()) for _ in range(ingredient_count)]
            cook_book[dishes_name] = ingredient_list
    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int):
    cook_book = get_cook_book_from_file()
    shop_list = {}
    for dishe in dishes:
        if dishe not in cook_book.keys():
            print(f'Блюда {dishe} нет в рецептах, оно будет пропущено')
            continue
        for ingredient in cook_book.get(dishe):
            ingredient_name = ingredient.get('ingredient_name')
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {
                    'measure': ingredient.get('measure'),
                    'quantity': ingredient.get('quantity') * person_count
                }
            else:
                shop_list[ingredient_name]['quantity'] += ingredient.get('quantity') * person_count
    return shop_list


if __name__ == '__main__':
    shop_list = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1)
    print(shop_list)
