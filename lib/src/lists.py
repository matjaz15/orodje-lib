def merge_and_sum_by_id(data, unique_id_name, sum_key_names=[]) -> list:
    """
    Merge objects with the same unique_id_name into single objects. Data is 
    taken from first merged object. if sum_key_names is give, also do a sum.

    :param list data: List of dictionaries.
    :param str unique_id_name: Merge dictionaries by this key name.
    :param list sum_key_names: Dictionaries with these keys will be summed.
    :return: List with dictionary-unique-key data.
    :rtype: list
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
    Convert table-like list data (ex. from a csv file) into object list data.

    :param list table_list: List of lists where fist list MUST have column names / headers as string.
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
        
        # Make sure that the number of row elements is the same as the number of columns.
        # You can't have more row elements than there are column elements.
        headers = table_list[0]
        items = table_list[i]
        row = {headers[j]: col for j, col in enumerate(items[:len(headers)])}
        
        
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