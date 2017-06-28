from reports import *

FILENAME = 'game_stat.txt'
TITLE = 'Counter-Strike'

output = open('report.txt', 'w')
output.write('Title of most played game(sold most): ' + str(get_most_played(FILENAME)) + '\n')
output.write('Total number of copies sold: ' + str(sum_sold(FILENAME)) + '\n')
output.write('Avg selling ammount is: ' + str(get_selling_avg(FILENAME)) + '\n')
output.write('The longest title is ' + str(count_longest_title(FILENAME)) + ' characters long!' + '\n')
output.write('Average release date is: ' + str(get_date_avg(FILENAME)) + '\n')
output.write('Properties of ' + TITLE + ': ' + str(get_game(FILENAME, TITLE)) + '\n')
output.write('Number of games based on genre: ' + str(count_grouped_by_genre(FILENAME)) + '\n')
output.write('Date ordered list of games: ' + str(get_date_ordered(FILENAME)) + '\n')
output.close()

print('Export done!')
