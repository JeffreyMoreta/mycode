#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


def farm_type(farm_name, result_type=None):
    for farm in farms:
        if farm.get('name') == farm_name:
            if result_type == "animals":
                result = return_animals(farm)
            else:
                result = farm.get('agriculture')

            return result


def return_animals(farm):
    valid_animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]
    return [animal for animal in farm.get('agriculture') if animal in valid_animals]


def user_input():
    response = input("Which farm would you like to look up? (NE Farm, W Farm, or SE Farm)")
    valid_farms = ["NE FARM", "W FARM", "SE FARM"]

    while not response.upper().strip() in valid_farms:
        print("Please input the correct farm name")
        response = input("Which farm would you like to look up? (NE Farm, W Farm, or SE Farm)")

    return response


def main():
    print("Challenge 1, NE Farm - all animals", farm_type("NE Farm", "animals"))
    print("Challenge 2, User Farm - all agriculture", farm_type(user_input()))
    print("Challenge 3, User Farm - all animals", farm_type(user_input(), "animals"))


if __name__ == "__main__":
    main()
