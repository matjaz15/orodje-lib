from csv import reader, writer
from xlrd import open_workbook

def read_csv_to_table(path, header_list=[], delimiter=',', encoding='utf-8') -> list:
    """
    Read CSV data into a table-like list, where the first list contains column names.

    :param str path: Absoulute file path.
    :param list header_list: List of strings, representing column names. Use if CSV has no headers
    :param str delimiter: CSV delimiter.
    :param str encoding: CSV encoding.
    :return: table-like list data.
    :rtype: list
    """

    file = open(path, "r", encoding=encoding)
    csv_reader = reader(file, delimiter=delimiter)    
    my_list = list(csv_reader)    
    file.close()
    if header_list:
        my_list.insert(0, header_list)
    return my_list

def write_csv_to_table(path, data_list, delimiter=',', encoding='utf-8', newline='') -> None:
    """
    Write table data into a CSV file.

    :param str path: Absoulute file path.
    :param list data_list: Data to write in the CSV file.
    :param str delimiter: CSV delimiter.
    :param str encoding: CSV encoding.
    :rtype: None
    """

    file = open(path, "w", encoding=encoding, newline=newline)
    csv_writer = writer(file, delimiter=delimiter)
    for row in data_list:
        csv_writer.writerow(row)
    file.close()

def read_xls_to_table(path) -> list:
    """
    Read XLS data into a table-like list.

    :param str path: Absoulute file path.
    :return: table-like list data.
    :rtype: list
    """

    book = open_workbook(path)
    sheet = book.sheet_by_index(0)
    return [[c.value for c in sheet.row(n)] for n in range(0, sheet.nrows)]