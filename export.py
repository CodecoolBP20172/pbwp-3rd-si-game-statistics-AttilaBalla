from reports import *

FILENAME = 'game_stat.txt'
DECIDE_YEAR = 2000
GENRE = 'RPG'
TITLE = 'Counter-Strike'

output = open('report.txt', 'w')
output.write('number of games in file: ' + str(count_games(FILENAME)) + '\n')
output.write('is there a game from year' + str(DECIDE_YEAR) + '?' + str(decide(FILENAME, DECIDE_YEAR)) + '\n')
output.write('latest game in this list is: ' + get_latest(FILENAME) + '\n')
output.write('number of games that match genre -' + GENRE + ':' + str(count_by_genre(FILENAME, GENRE)) + '\n')
output.write('line number of game' + TITLE + ':' + str(get_line_number_by_title(FILENAME, TITLE)) + '\n')
output.write('sorted list: ' + str(sort_abc(FILENAME)) + '\n')
output.write('sorted genre list: ' + str(get_genres(FILENAME)) + '\n')
output.write('The top FPS was released in: ' + str(when_was_top_sold_fps(FILENAME)) + '\n')
output.close()

print('Export done!')
