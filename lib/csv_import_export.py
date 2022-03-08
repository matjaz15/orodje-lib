from src.files import read_csv_to_table, write_csv_to_table
from src.lists import table_to_object, object_to_table

def import_csv_data(path, new_line_key, search_data_list, target_data_list=[], header_list=[], delimiter=',', encoding='utf-8') -> list:
    """
    Import CSV data into object data.

    :param str path: Absoulute file path.
    :param str new_line_key: New data line indicator.
    :param list search_data_list: Headers to search with.
    :param list target_data_list: Replaces search_data_list field names with target_data_list (indexees must match search_data_list).
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

def export_csv_data(path, object_data_list, delimiter=',', encoding='utf-8') -> None:
    """
    Export object data into a CSV file.

    :param str path: Absoulute file path with name and mime type.
    :param list object_data_list: Data list to export.
    :param str delimiter: CSV delimiter.
    :param str encoding: CSV encoding.
    :rtype: None
    """
    table_list_data = object_to_table(
        object_list = object_data_list
    )
    write_csv_to_table(
        path=path,
        data_list=table_list_data
    )
    return True