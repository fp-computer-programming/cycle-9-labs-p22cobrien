# Author: CMOB 1/11/2022

def add_food(lst):
    sixth_letter = []
    not_foods = []
    short_foods = []
    try:
        for index, value in enumerate(lst):
            try:
                if len(value) >= 6:
                    sixth_letter.append(value[5])
                elif len(value) < 6:
                    short_foods.append(value)
            except TypeError:
                not_foods.append(value)

    finally:
        print("Sixth_letter:", sixth_letter)
        print("Short_foods:", short_foods)
        print("Not_foods:", not_foods)



add_food(['potatoes','salsa','cherries','banana','apple'])
add_food(['naan','celery','buckwheat',7,'clementine'])
add_food(['cheeseburger',True, 'chicken','rice','radish'])