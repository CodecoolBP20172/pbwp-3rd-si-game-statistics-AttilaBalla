from reports import *
import pprint
pp = pprint.PrettyPrinter(width=100)
FILENAME = 'game_stat.txt'
TITLE = 'Counter-Strike'
pp.pprint('Title of most played game(sold most): ' + str(get_most_played(FILENAME)) + '\n')
pp.pprint('Total number of copies sold: ' + str(sum_sold(FILENAME)) + '\n')
pp.pprint('Avg selling ammount is: ' + str(get_selling_avg(FILENAME)) + '\n')
pp.pprint('The longest title is ' + str(count_longest_title(FILENAME)) + ' characters long!' + '\n')
pp.pprint('Average release date is: ' + str(get_date_avg(FILENAME)) + '\n')
pp.pprint('Properties of ' + TITLE + ': ' + str(get_game(FILENAME, TITLE)) + '\n')
pp.pprint('Number of games based on genre: ' + str(count_grouped_by_genre(FILENAME)) + '\n')
pp.pprint('Date ordered list of games: ' + str(get_date_ordered(FILENAME)) + '\n')
