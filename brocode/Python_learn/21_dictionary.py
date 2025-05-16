# dictionary = a collection of {key: value} pairs, ordered and changeable. NO duplicates

capitals = {"USA": "Washington DC",
    "India": "New Delhi",
    "Russia": "Moscow",
    "Japan": "Tokyo"}

# print(dir(capitals))
#['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# print(help(capitals))
# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital does not exist")

###################

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("Japan")
# capitals.popitem()
# capitals.clear()

# print(capitals["USA"])
# print(capitals)

# keys = capitals.keys()
# print(keys)

# for key in capitals.keys():
#     print(key)

# values = capitals.values()

# for value in capitals.values():
#     print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")



