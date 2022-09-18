# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]  # working


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]  # working


def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] += num


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, pet_breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            pets.append(pet["breed"])
    return pets


def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None


def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customers):
    return customers["cash"]


def remove_customer_cash(customers, cash):
    customers["cash"] -= cash


def get_customer_pet_count(customers):
    return len(customers["pets"])


def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False


def sell_pet_to_customer(pet_shop, pet, customer):
    # # Is the pet name in the pet_shop?
    pet_names = []

    for pets in pet_shop["pets"]:
        pet_names.append(pets["name"])
    # print(pet_names)

    if pets["name"] in pet_names and customer["cash"] >= pet["price"]:

        customer["pets"].append(pet)

        pet_shop["admin"]["pets_sold"] += 1

        customer["cash"] -= pet["price"]

        pet_shop["admin"]["total_cash"] += pet["price"]
    # for pets in pet_shop["pets"]:
    #     if pet == pets["name"] and customer["cash"] >= pet["price"]:
    #         customer["pets"].append(pet)

    print(customer["pets"])
    print("----------")
    print(pet)
    print("----------")
    print(pets["name"])
    print("----------")
    print(customer["cash"])
