def my_comp(lst):
    return [-el if 3<=el<=8 else el for el in lst]

print(my_comp([1,2,3,4,5,6,7,8,9,10]))