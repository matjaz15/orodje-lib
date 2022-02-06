def merge_and_sum_by_id(data, unique_id_name, sum_key_names):
    """Given an array of objects, merge objects with the same unique_id_name into single objects
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

    data = sorted(data, key = lambda i: (i[unique_id_name]))
    
    new_data = []
    current_id = None
    tmp = {}
    total_singles = 0
    for index, line in enumerate(data):       
        id = line[unique_id_name]

        if current_id != id:    
            if index > 0:
                new_data.append(tmp)
            current_id = id
            tmp = line
            total_singles = 0
        
        total_singles += 1
        if total_singles > 1:
            for k in sum_key_names:
                tmp[k] += line[k]

    new_data.append(tmp)
    return new_data


def table_to_object(table_list, new_line_key, search_data_list, target_data_list=False) -> list:
    """
    Convert table-like list data (ex. from a csv file) into structured object list data.

    :param list table_list: List of lists where fist list MUST have column names as string.
    :param str new_line_key: New data line indicator.
    :param list search_data_list: Headers to search with.
    :param list target_data_list: Replace search_data_list with target_data_list. Indexees must match search data.
    :return: structured object list data.
    :rtype: list
    """

    current_line = -1
    data = []
    vals = {}
    has_data = False

    for i in range(1, len(table_list)):
        # TODO: Preveri dolžino vrstic. Če je index stolpca višji od max indexa stolpcov v glavi, odreži
        # To pomeni, da prilagodiš podatke glede na glavo. 
        # Če je število stolpcov v vrstici manjše od število stolpcov v glavi, zapolni s False.

        row = {table_list[0][j]: col for j, col in enumerate(table_list[i])}
        
        if row[new_line_key] and current_line != row[new_line_key]:
            if int(current_line) >= 0:
                data.append(vals)
                vals = {}

            has_data = False
            current_line = row[new_line_key]

		# If is same data csv line and, the collumn has more values, create a list with values.
		# Assign the target_data_structure keys.
        for j, key in enumerate(search_data_list):
            val = row[key]            
            target_key = target_data_list[j] if target_data_list else key

            if not val or val == '':
                if not has_data:
                    vals[target_key] = False
                continue

            if not has_data:
                vals[target_key] = val
                continue

            if type(vals[target_key]) == list:
                vals[target_key].append(val)
                continue

            new_val = [val, vals[target_key]]
            vals[target_key] = new_val
        has_data = True

        if i >= len(table_list)-1:
            data.append(vals)

    return data