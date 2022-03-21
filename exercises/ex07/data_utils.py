"""Dictionary related utility functions."""

__author__ = "730475197"

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of csv into a table."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
    
    csv_reader = DictReader(file_handle)
    
    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table to a column-oriented table."""
    result: dict[str, list[str]] = dict()
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(a_dict: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Refers to top few rows of a table."""
    result: dict[str, list[str]] = dict()
    for column in a_dict:
        a_list: list[str] = []
        given_list: list[str] = a_dict[column]
        for rows in range(n):
            a_list.append(given_list[rows])
        result[column] = a_list
    return result


def select(a_dict: dict[str, list[str]], a_list: list[str]) -> dict[str, list[str]]:
    """Produces a simpler data table with only relevant subsets of original columns."""
    result: dict[str, list[str]] = dict()
    for name in a_list:
        result[name] = a_dict[name]
    return result


def concat(dict_a: dict[str, list[str]], dict_b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = dict()
    
    for column in dict_a:
        result[column] = dict_a[column]
    for columns in dict_b:
        result[columns] = dict_b[columns]
    keys_list_a = list(dict_a.keys())
    keys_list_b = list(dict_b.keys())
    for a_key in keys_list_a:
        for diff_key in keys_list_b:
            if a_key == diff_key:
                result[a_key] = dict_a[a_key] + dict_b[diff_key]

    return result


def count(values: list[str]) -> dict[str, int]:
    """Finds the frequency of the items in a given list."""
    result: dict[str, int] = {}                       
    for x in values:
        i: int = 0  
        j: int = 0
        while i < len(values):
            if x == values[i]:
                j += 1
                i += 1
            else:
                i += 1
        result[x] = j
    return result