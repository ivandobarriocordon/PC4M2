import math
from decimal import Decimal

my_list = ["Naia", "Ivan", "Astrid", "Max"]
my_dictionary = {
  "Group 1": ["Naia","Ivan","Astrid","Max"],
  "Group 2": ["Andoni","Josu"],
  "Group 3": ["Oier","Ruben"]
}
my_tuple = ("Naia", "Ivan", "Astrid", "Max")
my_integer = 17
my_float = 17.5
my_decimal = Decimal(17.57671)

my_float = math.ceil(my_float)
my_square_root = math.sqrt(my_float)

print(my_dictionary["Group 1"][0:1])
print(my_tuple[1])

my_list.append("Xavier")

print(my_list)

my_list[0] = "Alessandra"

print(my_list)

my_list.sort()

print(my_list)

my_tuple += ("Xavier",)

print(my_tuple)