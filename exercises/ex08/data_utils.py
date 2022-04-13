"""Utility functions for CSV files."""


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of csv into a 'table'."""
    result: list[dict[str, str]] = []    

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Read data file as CSV rather than just strings
    csv_reader = DictReader(file_handle)
    
    # Read each row of CSV line by line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
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
        if n > len(a_dict[column]):
            n = len(a_dict)
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


def count(values: list[str]) -> dict[str, int]:
    """Finds the frequency of the items in a given list."""
    result: dict[str, int] = {}                       
    for x in values:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result


def support(list_1: list[str], list_2: list[str]) -> list[str]:
    "If 2 lists have "
    result: list[str] = []
    for x in range(len(list_1)):
        if int(list_1[x]) >= 5:                 # compare high note taking
            if int(list_2[x]) >= 5:
                result.append("yes")
            else:
                result.append("no")
        else:
            if int(list_2[x]) >= 5:
                result.append("no")
            else:
                result.append("yes")
    return result