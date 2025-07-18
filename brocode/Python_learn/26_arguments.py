# default arguments = A default value for certain parameters default is used when that argument is omitted make your functions more flexible, reduces # of arguments
# 1. positional, 2.default 3.keyword 4. arbitrary

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

# # print(net_price(500))
# # print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))

##############################################

# import time

# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")
    
# count(30, 25)

###################################################
####################################################

# keyword arguments = an argument preceded by an identifier helps with readability order of arguments doesn't matter
# 1. positional, 2.default 3.keyword 4. arbitrary

# def hello(greeting, title, first, last):
#     print(f"{greeting}, {title} {first} {last}")
    
# hello("Hello", title="Mr.", last="John", first="James")

#######################################

# print("1", "2", "3", sep="-")

########################

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# print(get_phone(country=1, area=123, first=456, last=7890))


###################################################
####################################################

# arbitrary arguments 
# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
# * unpacking operator
# 1. positional, 2.default 3.keyword 4. arbitrary

# *args = type (tuple)
# def add(*args): # name is not imp can use *nums as well
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

###################################

# def display_name(*args):
#     for arg in args:
#         print(arg, end=' ')
        
# display_name("Dr.", "John", "Doe")

######################################
# **kwargs = type (dict)


# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street="123 Main St",
#               apt="100",
#               city="Anytown", 
#               state="CA", 
#               zipcode="12345")

########################################

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zipcode')}")

shipping_label("Dr.", "John", "Doe", "III",
               street="123 Main St",
               pobox= "PO box #1001",
            #    apt="100",
               city="Anytown",
               state="CA",
               zipcode="12345")