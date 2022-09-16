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
    count = 0
    for pet in pet_shop["pets"]:
        count += 1
    return count  # working


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
