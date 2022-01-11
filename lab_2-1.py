# Auhtor: CMOB 1/10/2022

def double_stuff(lst):
    for index, value in enumerate(lst):
        lst[index] = value * 2
    return lst


print(double_stuff([1, 3, 5, 4]) == [2, 6, 10, 8])
print(double_stuff([1, 2, 5, 7.5]) == [2, 4, 10, 15.0])
print(double_stuff([1, 2, 7.5, "a"]) == [2, 4, 15.0, "aa"])
