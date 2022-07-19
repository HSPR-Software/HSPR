def get_index_position(list_of_elems, element):
    """Returns the indexes of all occurrences of give element in
    the list- listOfElements

    Args:
        list_of_elems ([list]): [contains the names of the adb lines]
        element ([str]): [the line, which is being searched]

    Returns:
        [list]: [contain the indexs in list_of_elems which contains the element]
    """
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list 