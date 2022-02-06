from src.files import read_csv_to_table
from src.lists import table_to_object

def grab_csv_data(path, new_line_key, search_data_list, target_data_list=[], header_list=[], delimiter=',', encoding='utf-8') -> list:
    """
    Convert CSV data into object data.

    :param str path: Absoulute file path.
    :param str new_line_key: New data line indicator.
    :param list search_data_list: Headers to search with.
    :param list target_data_list: Replace search_data_list with target_data_list. Indexees must match search data.
    :param list header_list: List of strings, representing column names. Warning: use only if CSV has no headers.
    :param str delimiter: CSV delimiter.
    :param str encoding: CSV encoding.
    :return: structured object list data.
    :rtype: list
    """

    table_list_data = read_csv_to_table(
        path=path,
        header_list=header_list,
        delimiter=delimiter,
        encoding=encoding
    )
    object_data = table_to_object(
        table_list=table_list_data, 
        new_line_key=new_line_key, 
        search_data_list=search_data_list, 
        target_data_list=target_data_list
    )
    return object_data

