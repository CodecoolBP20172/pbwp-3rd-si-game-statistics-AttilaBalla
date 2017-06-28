import sys
import math
from collections import OrderedDict
FILENOTFOUND_FAILMSG = 'Failed to import file! check path or filename!'
STRTOINT_FAILMSG = 'Failed to convert str to int, check formatting in input file!'
STRTOFLOAT_FAILMSG = 'Failed to convert str to float, check formatting in input file!'


def import_file(file_name):  # helper function to handle file import
    try:
        dataset = [row.split('\t') for row in open(file_name)]
    except FileNotFoundError:
        return None
    return dataset


def get_most_played(file_name):
    largest_sold = 0
    largest_index = 0
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            try:
                ammount = float(dataitem[1])
            except ValueError:
                sys.exit(STRTOFLOAT_FAILMSG)
            if ammount > largest_sold:
                largest_sold = ammount
                largest_index = data.index(dataitem)
        return data[largest_index][0]

    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def sum_sold(file_name):
    result = 0
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            try:
                result += float(dataitem[1])
            except ValueError:
                sys.exit(STRTOFLOAT_FAILMSG)
        return result

    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def get_selling_avg(file_name):
    result = 0
    counter = 0
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            try:
                result += float(dataitem[1])
                counter += 1
            except ValueError:
                sys.exit(STRTOFLOAT_FAILMSG)
        return result/counter

    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def count_longest_title(file_name):
    result = 0
    longest_title = 0
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            if len(dataitem[0]) > longest_title:
                longest_title = len(dataitem[0])
        return longest_title
    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def get_date_avg(file_name):
    result = 0
    counter = 0
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            try:
                result += int(dataitem[2])
                counter += 1
            except ValueError:
                sys.exit(STRTOINT_FAILMSG)
        return math.ceil(result/counter)

    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def get_game(file_name, title):
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            if dataitem[0] == title:
                result = data[data.index(dataitem)]
                try:
                    result[1] = float(result[1])
                    result[2] = int(result[2])
                    result[4] = result[4].strip()
                except ValueError:
                    sys.exit('get_game: Failed to convert from str to int/float - check input file formatting!')
                return result
    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def count_grouped_by_genre(file_name):
    result = {}
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            if dataitem[3] not in result:
                result[dataitem[3]] = 1
            else:
                result[dataitem[3]] += 1
        return result
    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def get_date_ordered(file_name):
    titles_by_year = {}
    result = []
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            try:
                year = int(dataitem[2])
            except ValueError:
                sys.exit(STRTOINT_FAILMSG)

            if year not in titles_by_year:
                titles_by_year[year] = [dataitem[0]]
            else:
                titles_by_year[year].append(dataitem[0])
        sorted_dict = OrderedDict(sorted(titles_by_year.items(), key=lambda t: t[0], reverse=True))
        for key, value in sorted_dict.items():
            value = sorted(value)
            result += value
        return result

    else:
        sys.exit(FILENOTFOUND_FAILMSG)
