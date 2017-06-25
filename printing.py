from reports import *
import pprint
pp = pprint.PrettyPrinter(width=100)
FILENAME = 'game_stat.txt'
DECIDE_YEAR = 2000
GENRE = 'RPG'
TITLE = 'Counter-Strike'
pp.pprint('number of games in file: ' + str(count_games(FILENAME)))
pp.pprint('is there a game from year' + str(DECIDE_YEAR) + '? ' + str(decide(FILENAME, DECIDE_YEAR)))
pp.pprint('latest game in this list is: ' + get_latest(FILENAME))
pp.pprint('number of games that match genre - ' + GENRE + ': ' + str(count_by_genre(FILENAME, GENRE)))
pp.pprint('line number of game' + TITLE + ': ' + str(get_line_number_by_title(FILENAME, TITLE)))
pp.pprint('sorted list: ' + str(sort_abc(FILENAME)))
pp.pprint('sorted genre list: ' + str(get_genres(FILENAME)))
pp.pprint('The top FPS was released in: ' + str(when_was_top_sold_fps(FILENAME)))
