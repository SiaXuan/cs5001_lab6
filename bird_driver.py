'''
   CS5001
   Lab 6
   Spring 2025
   Sia Xuan
'''
from animal_analysis import create_name_dictionary, \
     create_habitat_dictionary, create_names_habitat_dictionary, \
     count_habitat_type
from bird_constants import COMMON_BIRDS, SCIENTIFIC_BIRDS, NEST_TYPES
common_names = COMMON_BIRDS
scientific_names = SCIENTIFIC_BIRDS
habitats = NEST_TYPES


def main():
    '''
    enter bird of feathere menu
    '''
    print("Here's the common names and their "
          "corresponding scientific names", end="")
    name_d = create_name_dictionary(common_names, scientific_names)
    print(name_d)
    print("Here's the common names and their "
          "corresponding scientific names, habitats", end="")
    d = create_names_habitat_dictionary(common_names,
                                        scientific_names,
                                        habitats)
    print(d)
    habitat = "platform"
    habitat_d = create_habitat_dictionary(common_names, habitats)
    number = count_habitat_type(habitat_d, habitat)
    print("There are", number, "type of birds live in " + habitat)


if __name__ == "__main__":
    main()
