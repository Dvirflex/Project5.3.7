
def chocolate_maker(small, big, x):
    chocolate_small_unit = small
    chocolate_big_unit = big * 5
    chocolate_length = chocolate_small_unit + chocolate_big_unit
    if chocolate_length >= x:
        return True
    else:
        return False


print(chocolate_maker(8, 2, 10))