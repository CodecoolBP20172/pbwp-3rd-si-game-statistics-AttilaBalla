import sys
FILENOTFOUND_FAILMSG = 'Failed to import file! check path or filename!'
STRTOINT_FAILMSG = 'Failed to convert str to int, check formatting in input file!'


def import_file(file_name):  # helper function to handle file import
    try:
        dataset = [row.split('\t') for row in open(file_name)]
    except FileNotFoundError:
        return None
    return dataset


def stringsort(stringlist):
    i = 1
    while i < len(stringlist):
        j = 0
        while j <= len(stringlist)-2:
            if str.capitalize(stringlist[j]) > str.capitalize(stringlist[j+1]):
                temp = stringlist[j+1]
                stringlist[j+1] = stringlist[j]
                stringlist[j] = temp
            j = j + 1
        i = i + 1
    return stringlist


def count_games(file_name):
    return len(import_file(file_name))


def decide(file_name, year):
    list_of_years = []
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            try:
                list_of_years.append(int(dataitem[2]))
            except ValueError:
                sys.exit('decide: ', STRTOINT_FAILMSG)
        if year in list_of_years:
            return True
        else:
            return False
    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def get_latest(file_name):
    latest_year = 0
    latest_index = 0
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            try:
                year = int(dataitem[2])
            except ValueError:
                sys.exit(STRTOINT_FAILMSG)
            if year > latest_year:
                latest_year = year
                latest_index = data.index(dataitem)
        return data[latest_index][0]

    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def count_by_genre(file_name, genre):
    genre_counter = 0
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            if dataitem[3] == genre:
                genre_counter += 1
        return genre_counter

    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def get_line_number_by_title(file_name, title):
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            if dataitem[0] == title:
                return data.index(dataitem)+1

    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def sort_abc(file_name):
    unsorted_list = []
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            unsorted_list.append(dataitem[0])
        return (stringsort(unsorted_list))

    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def get_genres(file_name):
    unsorted_genres = []
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            if dataitem[3] not in unsorted_genres:
                unsorted_genres.append(dataitem[3])
        return stringsort(unsorted_genres)

    else:
        sys.exit(FILENOTFOUND_FAILMSG)


def when_was_top_sold_fps(file_name):
    top_sellcount = 0
    year_of_release = 0
    data = import_file(file_name)
    if data is not None:
        for dataitem in data:
            try:
                sellcount = float(dataitem[1])
            except ValueError:
                sys.exit(STRTOINT_FAILMSG)

            if sellcount > top_sellcount and dataitem[3] == 'First-person shooter':
                top_sellcount = sellcount
                year_of_release = int(dataitem[2])
        if year_of_release > 0:
            return year_of_release
        else:
            raise ValueError('There is no game that matches the required genre!')

    else:
        sys.exit(FILENOTFOUND_FAILMSG)
