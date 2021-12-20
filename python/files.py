import csv


"""--TEST--
path = "C:/../test.csv"
search_data_structure = ["Naziv","Cena kosila","Cena večerje","Cena zajtrka","Država/ID","Polna cena","Trajanje do","Trajanje od","Država/Koda države"]
target_data_structure = ['name','lunch_price','dinner_price','breakfast_price','country_ids','full_price','duration_to','duration_from','country_codes']
line_key = 'ID'
result = grab_csv_data(path, line_key, search_data_structure, target_data_structure)
"""
def grab_csv_data(path, line_key, search_data_structure, target_data_structure=False):
    """
    path: Absolute file path.
	line_key: New data line indicator.
	search_data_structure: Headers to search with.
    target_data_structure: If data given, use index value at current header index from search_data_structure as new key.
    """
    file = open(path, "r", encoding='utf-8')
    csv_reader = csv.reader(file, delimiter=',')
    my_list = list(csv_reader)

    current_line = -1
    data = []
    vals = {}
    has_data = False
    for i in range(1, len(my_list)):
        row = {my_list[0][j]: col for j, col in enumerate(my_list[i])}

        if row[line_key] and current_line != row[line_key]:
            if int(current_line) >= 0:
                data.append(vals)
                vals = {}

            has_data = False
            current_line = row[line_key]

		# If is same data csv line and, the collumn has more values, create a list with values.
		# Assign the target_data_structure keys.
        for j, key in enumerate(search_data_structure):
            val = row[key]
            target_key = target_data_structure[j] if target_data_structure else key

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

        if i >= len(my_list)-1:
            data.append(vals)
    return data