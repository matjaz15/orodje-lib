def merge_and_sum_by_id(data, unique_id_name, sum_key_names):
    """Given array of objects, merge objects with the same unique_id_name into single objects
    and sum fields with sum_key_names. Non sum_key_names fields are taken from first merged object.
    BEFORE:
    {'my_id': 1, 'name': 'test', 'num1': 5, 'num2': 10}
    {'my_id': 1, 'name': 'test2', 'num1': 2, 'num2': 3}
    {'my_id': 1, 'name': 'test3', 'num1': 1, 'num2': 2}
    {'my_id': 6, 'name': 'test4', 'num1': 4, 'num2': 5}
    merge_and_sum_by_id(data, 'my_id', ['num1', 'num2'])
    AFTER:
    {'my_id': 1, 'name': 'test', 'num1': 8, 'num2': 15}
    {'my_id': 6, 'name': 'test4', 'num1': 4, 'num2': 5}
    """
    
    new_data = []
    current_id = None
    tmp = {}
    for index, line in enumerate(data):       
        id = line[unique_id_name]

        if current_id != id or index >= len(data)-1:    
            if index > 0:
                new_data.append(tmp)
            current_id = id
            tmp = line
        
        for k in sum_key_names:
            tmp[k] += line[k]

    return new_data
