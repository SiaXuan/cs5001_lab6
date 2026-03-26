'''
   CS5001
   Lab 6
   Spring 2025
   Sia Xuan
'''


def create_name_dictionary(common_names: list, scientific_names: list) -> dict:
    '''pair the common_names with its scientific_names
    '''
    name_d = {}
    for i in range(len(common_names)):
        name_d[common_names[i]] = scientific_names[i]
    return name_d


def create_habitat_dictionary(common_names: list, habitats: list) -> dict:
    ''' pair the common_names with its habitats
    >>> a = ["bird1", "bird2", "bird3"]
    >>> h = ["h1","h2", "h1"]
    >>> create_habitat_dictionary(a, h)
    {'bird1': 'h1', 'bird2': 'h2', 'bird3': 'h1'}
    '''
    habitat_d = {}
    for i in range(len(common_names)):
        habitat_d[common_names[i]] = habitats[i]
    return habitat_d


def create_names_habitat_dictionary(common_names: list,
                                    scientific_names: list,
                                    habitats: list) -> dict:
    ''' pair the common_names with its scientific_names and habitats
    '''
    names_habitat_d = {}
    for i in range(len(common_names)):
        names_habitat_d[common_names[i]] = [scientific_names[i], habitats[i]]
    return names_habitat_d


def count_habitat_type(habitat_d: dict, habitat: str) -> int:
    '''
    Returns the number of animals in that dictionary
    with that exact string for its habitat.
    >>> habitat_d = {"bird1": "h1", "bird2": "h2", "bird3": "h1"}
    >>> count_habitat_type(habitat_d, "h1")
    2
    '''
    counter = 0
    for i in habitat_d.values():
        if habitat == i:
            counter += 1
    return counter


if __name__ == "__main__":
    main()
